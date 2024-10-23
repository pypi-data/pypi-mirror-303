from typing import List, Union, Optional, Literal

from collinear.BaseService import BaseService
from collinear.judge.types import ConversationMessage, CollinearGuardNanoOutput, \
    ScoringCriteria, ClassificationInput, PointwiseInput, CollinearGuardPointwiseOutput


class CollinearGuard(BaseService):
    def __init__(self, access_token: str) -> None:
        super().__init__(access_token)

    async def classification(self, model_type: Literal['prompt', 'response', 'refusal'],
                             conv_prefix: List[Union[ConversationMessage, dict]],
                             response: Union[ConversationMessage, dict],
                             scoring_criteria: Optional[List[ScoringCriteria]] = None) -> CollinearGuardNanoOutput:
        """
        Sends a classification request to the Collinear Guard Nano model.
        Args:
            model_type (Literal['prompt', 'response', 'refusal']): The type of model to use.
                Allowed values are 'prompt', 'response', 'refusal'.
            response (Union[ConversationMessage, dict]): The response to be evaluated.
                Should be either a ConversationMessage object or a dict with 'role' and 'content' keys.
                Example: {"role": "assistant", "content": "How can I help you today?"}
            conv_prefix (List[Union[ConversationMessage, dict]]): The conversation history.
                Each message should be either a ConversationMessage object or a dict with 'role' and 'content' keys.
                Example: [{"role": "user", "content": "Hello"}, {"role": "assistant", "content": "Hi there!"}]
            scoring_criteria (List[ScoringCriteria]): The scoring criteria to use for the classification. This is optional.
        Raises:
            ValueError: If scoring criteria is not None and does not have 2 elements

        Returns:
            CollinearGuardNanoOutput: Contains judgement

        """
        if scoring_criteria is not None and len(scoring_criteria) != 2:
            raise ValueError("Scoring criteria should have 2 elements")
        input_data = ClassificationInput(
            nano_model_type=model_type,
            conversation=conv_prefix,
            response=response,
            scoring_criteria=scoring_criteria
        )
        response = await self.send_request('/api/v1/judge/safety', "POST", {
            'model_name': 'collinear_guard_classifier',
            **input_data.dict()
        })
        return CollinearGuardNanoOutput(judgement=response['judgement'])

    async def pointwise(self,
                        conv_prefix: List[Union[ConversationMessage, dict]],
                        response: Union[ConversationMessage, dict],
                        scoring_criteria: Optional[List[ScoringCriteria]] = None
                        ) -> CollinearGuardPointwiseOutput:
        """
        Sends a pointwise request to the Collinear Guard model.
        Args:
            response (Union[ConversationMessage, dict]): The response to be evaluated.
                Should be either a ConversationMessage object or a dict with 'role' and 'content' keys.
                Example: {"role": "assistant", "content": "How can I help you today?"}
            conv_prefix (List[Union[ConversationMessage, dict]]): The conversation history.
                Each message should be either a ConversationMessage object or a dict with 'role' and 'content' keys.
                Example: [{"role": "user", "content": "Hello"}, {"role": "assistant", "content": "Hi there!"}]
            scoring_criteria (List[ScoringCriteria]): The scoring criteria to use for the classification. This is optional.
        Raises:
            ValidationError: If any validation error occurs
        Returns:
            CollinearGuardPointwiseOutput: Contains judgement and rationale


        """
        input_data = PointwiseInput(
            conversation=conv_prefix,
            response=response,
            scoring_criteria=scoring_criteria
        )
        response = await self.send_request('/api/v1/judge/safety', "POST", {
            'model_name': 'collinear_guard',
            **input_data.dict()
        })

        return CollinearGuardPointwiseOutput(judgement=response['judgement'], rationale=response['extra']['rationale'])
