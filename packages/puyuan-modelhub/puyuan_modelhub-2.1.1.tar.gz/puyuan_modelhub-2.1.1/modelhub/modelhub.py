from ._async_modelhub import AsyncModelhub
from ._sync_modelhub import SyncModelhub


class ModelhubClient:
    def __init__(self, *args, **kwargs):
        _sync = SyncModelhub(*args, **kwargs)
        _async = AsyncModelhub(*args, **kwargs)
        self.chat = _sync.chat
        self.get_embeddings = _sync.get_embeddings
        self.stream_chat = _sync.stream_chat
        self.stream = _sync.stream_chat
        self.cross_embedding = _sync.cross_embedding
        self.count_tokens = _sync.count_tokens
        self.n_tokens = _sync.count_tokens
        self.transcribe = _sync.transcribe
        self.supported_models = _sync.supported_models

        self.achat = _async.chat
        self.aget_embeddings = _async.get_embeddings
        self.astream_chat = _async.stream_chat
        self.astream = _async.stream_chat
        self.across_embedding = _async.cross_embedding
        self.acount_tokens = _async.count_tokens
        self.an_tokens = _async.count_tokens
        self.atranscribe = _async.transcribe
