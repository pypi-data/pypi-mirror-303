from typing import Any, Dict, List, Literal, Optional
from modelhub.types._base import BaseModel


class TextGenerationStreamToken(BaseModel):
    text: str


class TextGenerationDetails(BaseModel):
    finish_reason: Literal[
        "stop", "length", "tool_calls", "content_filter", "function_call"
    ] | None = "stop"
    created: Optional[int] = None
    model: Optional[str] = None
    request_time: Optional[float] = None
    prompt_tokens: Optional[int] = None
    generated_tokens: Optional[int] = None


class BaseOutput(BaseModel):
    code: int = 200
    msg: str = "success"

    class Config:
        extra = "allow"


class FunctionOutput(BaseModel):
    arguments: str
    name: str


class ToolCallOutput(BaseModel):
    id: str
    function: FunctionOutput
    type: Literal["function"] = "function"


class TextGenerationStreamOutput(BaseOutput):
    token: TextGenerationStreamToken
    tool_calls: Optional[List[ToolCallOutput]] = None
    details: Optional[TextGenerationDetails] = None


class TextGenerationOutput(BaseOutput):
    generated_text: str
    tool_calls: Optional[List[ToolCallOutput]] = None
    details: Optional[TextGenerationDetails] = None


class ErrorMessage(BaseOutput):
    code: int = 500
    msg: str = "failed"


class ModelInfo(BaseModel):
    types: List[Literal["chat", "embedding", "audio", "reranker"]]

    class Config:
        extra = "allow"


class ModelInfoOutput(BaseOutput):
    models: Dict[str, ModelInfo]


class ModelParamsOutput(BaseOutput):
    param_schema: Dict[str, Any]


class NTokensOutput(BaseOutput):
    n_tokens: int


class EmbeddingOutput(BaseOutput):
    embeddings: List[List[float]] | None = None
    weights: List[Dict[int, float]] | None = None
