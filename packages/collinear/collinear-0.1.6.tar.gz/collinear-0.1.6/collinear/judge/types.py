from typing import Literal, List, Optional

from pydantic import BaseModel


class ConversationMessage(BaseModel):
    """
       Represents a single message in a conversation.

       Attributes:
           content (str): The text content of the message.
           role (Literal["user", "assistant", "system"]): The role of the entity sending the message.
               Must be one of "user", "assistant", or "system".

       Example:
           >>> message = ConversationMessage(content="Hello, how can I help?", role="assistant")
       """
    content: str
    role: Literal["user", "assistant", "system"]


class ConversationInput(BaseModel):
    context: str
    conversation: List[ConversationMessage]
    response: ConversationMessage

    class Config:
        populate_by_name = True


class VeritasOutput(BaseModel):
    """
       Represents the output from the Veritas judgment system.

       Attributes:
           judgement (int): The numerical judgment. 1 means the input is factual, 0 means it is hallucinated.
           score (float): A float value representing an additional scoring metric.

       Example:
           >>> output = VeritasOutput(judgement=8, score=0.95)
       """
    judgement: int
    score: float


class CollinearGuardNanoOutput(BaseModel):
    """
    Represents the output from the Collinear Guard Nano system.

    Attributes:
        judgement (int): The numerical judgement. 1 means the input is safe, 0 means it is unsafe.

    Example:
        >>> output = CollinearGuardNanoOutput(judgement=8)
    """
    judgement: int


class ScoringCriteria(BaseModel):
    """
    Represents the scoring criteria for the Collinear Guard.

    Attributes:
        score (float): The score to assign to a scoring criteria
        description (str): Description you want to give to the scoring criteria

    Example:
        >>> criteria = ScoringCriteria(factual_score=1.0, hallucinated_score=0.0)
    """
    score: int
    description: str

class CollinearGuardPointwiseOutput(BaseModel):
    """
    Represents the output from the Collinear Guard model.

    Attributes:
        judgement (int): The numerical judgement. It can range based on scoring criteria.
        rationale (str): The rationale for the judgement.
    Examples:
          >>> output = CollinearGuardPointwiseOutput(judgement=5, rationale="The response is safe.")

    """
    judgement: int
    rationale: str

class ClassificationInput(BaseModel):
    nano_model_type: Literal['prompt', 'response', 'refusal']
    conversation: List[ConversationMessage]
    response: ConversationMessage
    scoring_criteria: Optional[List[ScoringCriteria]] = None

class PointwiseInput(BaseModel):
    conversation: List[ConversationMessage]
    response: ConversationMessage
    scoring_criteria: Optional[List[ScoringCriteria]] = None