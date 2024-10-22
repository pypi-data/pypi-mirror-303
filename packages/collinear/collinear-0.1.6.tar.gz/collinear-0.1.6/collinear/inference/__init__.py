import asyncio
import uuid

import pandas as pd
from tqdm.asyncio import tqdm
from asynciolimiter import Limiter

from collinear.BaseService import BaseService


class Inference(BaseService):
    def __init__(self, access_token: str) -> None:
        super().__init__(access_token)

    async def run_inference_on_dataset(self, data: pd.DataFrame,
                                       conv_prefix_column_name: str,
                                       model_id: uuid.UUID,
                                       generation_kwargs={},
                                       calls_per_second: int = 10,
                                       max_concurrent_tasks: int = 10) -> pd.DataFrame:

        # Check if the column exists in the dataframe
        if conv_prefix_column_name not in data.columns:
            raise ValueError(f"Column {conv_prefix_column_name} not found in the dataset")

        # Initialize an async progress bar
        pbar = tqdm(total=len(data))

        # Rate limiter and task limiter (for concurrent tasks)
        rate_limiter = Limiter(calls_per_second)
        semaphore = asyncio.Semaphore(max_concurrent_tasks)

        async def generate(example):
            async with semaphore:  # Limit concurrent tasks
                await rate_limiter.wait()  # Respect the rate limit
                body = {
                    "model_id": model_id,
                    "messages": example[conv_prefix_column_name],
                    "generation_kwargs": generation_kwargs
                }
                try:
                    output = await self.send_request('/api/v1/model/inference', "POST", body)
                    # Create a new dict instead of mutating the example
                    result = example.copy()
                    result['response'] = {'role': 'assistant', 'content': output}
                    return result
                except Exception as e:
                    # Log the error or handle it (e.g., add a failure message)
                    return {"error": str(e)}
                finally:
                    # Update the progress bar once the request completes
                    pbar.update(1)

        tasks = [generate(row) for idx, row in data.iterrows()]
        results = await asyncio.gather(*tasks)
        pbar.close()

        results_df = pd.DataFrame(results)
        return results_df
