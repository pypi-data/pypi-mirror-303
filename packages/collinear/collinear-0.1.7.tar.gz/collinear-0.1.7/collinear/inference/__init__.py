import asyncio
import logging
import uuid

import pandas as pd
from anthropic import AsyncAnthropic
from asynciolimiter import Limiter
from openai import AsyncOpenAI
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
from tqdm.asyncio import tqdm

from collinear.BaseService import BaseService
from collinear.model import Model
from collinear.model.types import ModelTypeEnum, ModelDTO


class Inference(BaseService):
    def __init__(self, access_token: str, model_service: Model) -> None:
        super().__init__(access_token)
        self.model = model_service

    @retry(retry=retry_if_exception_type(Exception),
           stop=stop_after_attempt(5),
           wait=wait_exponential(multiplier=1, min=4, max=10))
    async def get_chat_completion(self, model: ModelDTO, messages: list[dict], generation_kwargs={}) -> str:
        if model.type == ModelTypeEnum.openai:
            openai_client = AsyncOpenAI(base_url=model.base_url, api_key=model.api_key)
            completion = await openai_client.chat.completions.create(
                model=model.name,
                messages=messages,
                **generation_kwargs
            )
            return str(completion.choices.pop().message.content)
        elif model.type == ModelTypeEnum.anthropic:
            logging.debug("Using Anthropic client")
            anthropic_client = AsyncAnthropic(api_key=model.api_key, base_url=model.base_url)
            message = await anthropic_client.messages.create(
                messages=messages,
                model=model.name,
                **generation_kwargs
            )
            logging.debug(f"Anthropic completion result: {message}")
            return str(message.content)
        else:
            logging.error(f"Unknown model type: {model.type}")
            raise ValueError(f"Unsupported model type: {model.type}")

    async def run_inference_on_dataset(self, data: pd.DataFrame,
                                       conv_prefix_column_name: str,
                                       model_id: uuid.UUID,
                                       generation_kwargs={},
                                       calls_per_second: int = 10,
                                       max_concurrent_tasks: int = 10) -> pd.DataFrame:

        # Check if the column exists in the dataframe
        if conv_prefix_column_name not in data.columns:
            raise ValueError(f"Column {conv_prefix_column_name} not found in the dataset")

        model = await self.model.get_model_by_id(model_id)
        # Initialize an async progress bar
        pbar = tqdm(total=len(data))

        # Rate limiter and task limiter (for concurrent tasks)
        rate_limiter = Limiter(calls_per_second)
        semaphore = asyncio.Semaphore(max_concurrent_tasks)

        async def generate(example):
            async with semaphore:  # Limit concurrent tasks
                await rate_limiter.wait()  # Respect the rate limit
                try:
                    value = await self.get_chat_completion(model, example[conv_prefix_column_name], generation_kwargs)
                    result = example.copy()
                    result['response'] = {'role': 'assistant', 'content': value}
                    return result
                except Exception as e:
                    return {"error": str(e)}
                finally:
                    pbar.update(1)

        tasks = [generate(row) for idx, row in data.iterrows()]
        results = await asyncio.gather(*tasks)
        pbar.close()

        results_df = pd.DataFrame(results)
        return results_df
