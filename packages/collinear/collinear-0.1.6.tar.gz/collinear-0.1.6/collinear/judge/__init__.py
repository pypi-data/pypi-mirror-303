import asyncio
import uuid

import pandas as pd

from collinear.BaseService import BaseService
from collinear.judge.collinear_guard import CollinearGuard
from collinear.judge.veritas import Veritas
from tqdm.asyncio import tqdm


class Judge(BaseService):
    def __init__(self, access_token: str) -> None:
        super().__init__(access_token)
        self._veritas = None
        self._collinear_guard = None

    @property
    def veritas(self):
        """
        Lazy-load Veritas service when accessed for the first time.
        Cache the result for subsequent accesses.
        """
        if self._veritas is None:
            self._veritas = Veritas(self.access_token)
        return self._veritas

    @property
    def collinear_guard(self):
        """
        Lazy-load Collinear Guard service when accessed for the first time.
        Cache the result for subsequent accesses.
        """
        if self._collinear_guard is None:
            self._collinear_guard = CollinearGuard(self.access_token)
        return self._collinear_guard

    async def run_judge_on_dataset(self,

                                   data: pd.DataFrame,
                                   conv_prefix_column_name: str,
                                   response_column_name: str,
                                   space_id: uuid.UUID,
                                   judge_id: uuid.UUID,
                                   judge_name: str) -> pd.DataFrame:
        if conv_prefix_column_name not in data.columns or response_column_name not in data.columns:
            raise ValueError(f"Column {conv_prefix_column_name} not found in the dataset")
        pbar = tqdm(total=len(data))

        async def generate(example):
            conv_prefix = [m for m in example[conv_prefix_column_name]]
            response = example[response_column_name]
            body = {
                "conversation_prefix": conv_prefix,
                "response": response,
                "space_id": space_id,
                "judge_id": judge_id
            }
            judgement = await self.send_request('/api/v1/judge/conversation', "POST", body)

            pbar.update(1)
            return {"conv_prefix": conv_prefix,
                    "response": response,
                    "judgements": {judge_name: judgement},
                    }

        tasks = []
        for idx, row in data.iterrows():
            tasks.append(asyncio.create_task(generate(row)))
        results = await asyncio.gather(*tasks)
        result_df = pd.DataFrame({
            'conv_prefix': [row['conv_prefix'] for row in results],
            'response': [row['response'] for row in results],
            'judgements': [row['judgements'] for row in results]
        })

        return result_df
