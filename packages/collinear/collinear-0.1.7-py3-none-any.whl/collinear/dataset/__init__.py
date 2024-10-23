import uuid

import pandas as pd

from collinear.BaseService import BaseService


class Dataset(BaseService):
    def __init__(self, access_token: str) -> None:
        super().__init__(access_token)

    async def upload_dataset(self, data: pd.DataFrame,
                             conv_prefix_column_name: str,
                             response_column_name: str,
                             judgement_column_name: str | None,
                             dataset_name: str,
                             space_id: uuid.UUID,
                             parent_dataset_id: uuid.UUID | None) -> uuid.UUID:
        req_obj = {
            "name": dataset_name,
            "space_id": space_id,
        }
        if parent_dataset_id:
            req_obj['parent_dataset_id'] = parent_dataset_id
        conversations = []
        for index, row in data.iterrows():
            obj = {
                'conv_prefix': list(row[conv_prefix_column_name]),
                'response': row[response_column_name]['content'],
                'judgements': row[judgement_column_name] if judgement_column_name in row else {}
            }
            conversations.append(obj)
        req_obj['conversations'] = conversations
        output = await self.send_request('/api/v1/dataset', "POST", req_obj)
        print(output)
        return output['dataset_id']
