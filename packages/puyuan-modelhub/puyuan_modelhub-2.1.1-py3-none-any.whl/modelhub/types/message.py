from ._base import BaseModel


class BaseMessage(BaseModel):
    role: str
    content: str


class SystemMessage(BaseMessage):
    role: str = "system"


class UserMessage(BaseMessage):
    role: str = "user"


class AIMessage(BaseMessage):
    role: str = "assistant"


class ToolMessage(BaseMessage):
    role: str = "tool"
