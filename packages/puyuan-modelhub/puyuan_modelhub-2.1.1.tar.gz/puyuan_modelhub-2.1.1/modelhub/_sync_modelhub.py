import os
from io import TextIOWrapper
from typing import Any, Dict, List, Literal, Optional, Union

import httpx

from modelhub.types import (
    BaseMessage,
    CrossEncoderOutput,
    CrossEncoderParams,
    ModelInfo,
    ModelInfoOutput,
    EmbeddingOutput,
    NTokensOutput,
    TextGenerationOutput,
    TextGenerationStreamOutput,
    Transcription,
)
from modelhub.types import errors as err

from ._sync_client import SyncAPIClient
from ._constants import DEFAULT_MAX_RETRIES, DEFAULT_TIMEOUT


PROMPT_TYPE = Union[
    str,
    List[Union[BaseMessage, Dict[str, Any]]],
    Union[BaseMessage, Dict[str, Any]],
]


class SyncModelhub:
    def __init__(
        self,
        host: Optional[str] = None,
        user_name: Optional[str] = None,
        user_password: Optional[str] = None,
        model: Optional[str] = None,
        max_retries: Optional[int] = DEFAULT_MAX_RETRIES,
        timeout: Optional[httpx.Timeout] = DEFAULT_TIMEOUT,
    ):
        base_url = host or os.getenv("MODELHUB_HOST")
        user_name = user_name or os.getenv("MODELHUB_USER_NAME")
        user_password = user_password or os.getenv("MODELHUB_USER_PASSWORD")
        if not base_url:
            raise ValueError("host URL is required")
        params = {
            "base_url": base_url,
            "max_retries": max_retries,
            "timeout": timeout,
            "auth_headers": {"Authorization": f"{user_name}:{user_password}"},
        }
        self._default_model = model
        self._client = SyncAPIClient(**params)
        self._get = self._client.get
        self._post = self._client.post
        self._stream = self._client.stream

    def _process_prompt(self, prompt: PROMPT_TYPE):
        if isinstance(prompt, list):
            return [m.dict() if isinstance(m, BaseMessage) else m for m in prompt]
        if isinstance(prompt, (BaseMessage, dict)):
            return [prompt.dict() if isinstance(prompt, BaseMessage) else prompt]
        prompt = self._replace_image_with_id(prompt)

        return prompt

    def _upload_image(self, image_path: str):
        res = self._post(
            "image/upload",
            options={"files": {"file": open(image_path, "rb")}},
            cast_to=Dict,
        )
        return res.json()["id"]

    def _replace_image_with_id(self, s: str):
        """extract image path from a markdown string"""
        import re

        match = re.fullmatch(r"!\[(.*?)\]\((.*?)\)", s)
        if not match:
            return s
        image_path = match.group(2)
        if not os.path.exists(image_path):
            return s
        image_id = self._upload_image(image_path)
        return f"![{match.group(1)}]({image_id})"

    def _prepare_chat_args(
        self,
        prompt: PROMPT_TYPE,
        model: Optional[str] = None,
        history: List[Union[BaseMessage, Dict[str, Any]]] = [],
        return_type: Literal["text", "json", "regex"] = "text",
        return_schema: Optional[Union[Dict[str, Any], str]] = None,
        parameters: Optional[Dict] = {},
        *,
        stream: bool = False,
        **kwargs,
    ):
        new_params = parameters.copy()
        model = model or self._default_model
        if isinstance(prompt, list) and history:
            raise err.BadParamsError(msg="prompt and history cannot both be lists")
        new_params["return_type"] = return_type
        new_params["schema"] = return_schema
        return {
            "prompt": self._process_prompt(prompt),
            "model": model,
            "parameters": {**new_params, **kwargs},
            "stream": stream,
        }

    def count_tokens(
        self,
        prompt: PROMPT_TYPE,
        model: Optional[str] = None,
        params: Optional[Dict[str, Any]] = {},
        timeout: Optional[httpx.Timeout] = None,
        **kwargs,
    ) -> int:
        res = self._post(
            "tokens",
            body={
                "prompt": self._process_prompt(prompt),
                "model": model or self._default_model,
                "params": {**params, **kwargs},
            },
            cast_to=NTokensOutput,
            options={"timeout": timeout},
        )
        return res.n_tokens

    def chat(
        self,
        prompt: PROMPT_TYPE,
        model: Optional[str] = None,
        history: List[Union[BaseMessage, Dict[str, Any]]] = [],
        return_type: Literal["text", "json", "regex"] = "text",
        return_schema: Union[Dict[str, Any], str, None] = None,
        parameters: Optional[Dict[str, Any]] = {},
        timeout: Optional[httpx.Timeout] = None,
        **kwargs,
    ) -> TextGenerationOutput:
        return self._post(
            "chat",
            body=self._prepare_chat_args(
                prompt=prompt,
                model=model,
                history=history,
                return_type=return_type,
                return_schema=return_schema,
                parameters=parameters,
                **kwargs,
            ),
            cast_to=TextGenerationOutput,
            options={"timeout": timeout},
        )

    def stream_chat(
        self,
        prompt: PROMPT_TYPE,
        model: Optional[str] = None,
        history: List[BaseMessage] = [],
        parameters: Dict[str, Any] = {},
        timeout: Optional[httpx.Timeout] = None,
        **kwargs,
    ):
        return self._stream(
            "chat",
            body=self._prepare_chat_args(
                prompt=prompt,
                model=model,
                history=history,
                parameters=parameters,
                stream=True,
                **kwargs,
            ),
            cast_to=TextGenerationStreamOutput,
            options={"timeout": timeout},
        )

    def get_embeddings(
        self,
        prompt: str,
        model: Optional[str] = None,
        parameters: Dict[str, Any] = {},
        timeout: Optional[httpx.Timeout] = None,
        **kwargs,
    ) -> EmbeddingOutput:
        return self._post(
            "embedding",
            body={
                "prompt": prompt,
                "model": model or self._default_model,
                "parameters": parameters,
            },
            cast_to=EmbeddingOutput,
            options={"timeout": timeout},
        )

    def cross_embedding(
        self,
        sentences: List[List[str]],
        model: Optional[str] = None,
        parameters: CrossEncoderParams = {},
        timeout: Optional[httpx.Timeout] = None,
        **kwargs,
    ) -> CrossEncoderOutput:
        return self._post(
            "cross_embedding",
            body={
                "sentences": sentences,
                "model": model or self._default_model,
                "parameters": {**parameters, **kwargs},
            },
            cast_to=CrossEncoderOutput,
            options={"timeout": timeout},
        )

    def transcribe(
        self,
        file: Union[str, TextIOWrapper],
        model: Optional[str] = None,
        language: str = "",
        temperature: float = 0.0,
        timeout: Optional[httpx.Timeout] = None,
    ) -> Transcription:
        model = model or self.model
        if isinstance(file, str):
            file = open(file, "rb")

        return self._post(
            "audio/transcriptions",
            files={"file": file},
            data={
                "model": model,
                "language": language,
                "temperature": temperature,
            },
            cast_to=Transcription,
            options={"timeout": timeout},
        )

    @property
    def supported_models(self) -> Dict[str, ModelInfo]:
        return self._get_supported_models()

    def _get_supported_models(self) -> ModelInfoOutput:
        """Get a list of supported models from the Modelhub API"""
        response = self._get("models", cast_to=ModelInfoOutput)
        return response.models
