from typing import Any, List

from typing_extensions import NotRequired, TypedDict

from .generation import BaseOutput


class HfCrossEncoderParams(TypedDict):
    batch_size: NotRequired[int]
    show_progress_bar: NotRequired[bool]
    num_workers: NotRequired[int]
    activation_fct: NotRequired[Any]
    apply_softmax: NotRequired[bool]
    convert_to_numpy: NotRequired[bool]
    convert_to_tensor: NotRequired[bool]

class CrossEncoderOutput(BaseOutput):
    scores: List[float]

CrossEncoderParams = HfCrossEncoderParams
