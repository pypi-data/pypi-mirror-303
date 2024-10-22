# Description

[PyPI](https://pypi.org/project/puyuan-modelhub/#description), [Github](https://github.com/puyuantech/modelhub)

📦 ModelhubClient: A Python client for the Modelhub. Support various models including LLMs, embedding models, audio models and multi-modal models. These models are implemented by either 3rdparty APIs or self-host instances.

# Installation

```shell
pip install puyuan_modelhub --user
```

# Current Supported Models

| name                         | pricing                     | context_window | is_local | description                                                                                                                                                                                                                                                             |
| :--------------------------- | :-------------------------- | -------------: | :------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Baichuan4                    | INPUT: 100¥, OUTPUT: 100¥   |          32768 | False    | 模型调用 Baichuan4                                                                                                                                                                                                                                                      |
| Baichuan3-Turbo              | INPUT: 12¥, OUTPUT: 12¥     |          32768 | False    | 模型调用 Baichuan3-Turbo                                                                                                                                                                                                                                                |
| Baichuan3-Turbo-128k         | INPUT: 24¥, OUTPUT: 24¥     |         128000 | False    | 模型调用 Baichuan3-Turbo-128k                                                                                                                                                                                                                                           |
| Baichuan2-Turbo              | INPUT: 8¥, OUTPUT: 8¥       |          32768 | False    | 模型调用 Baichuan2-Turbo                                                                                                                                                                                                                                                |
| Baichuan2-Turbo-192k         | INPUT: 16¥, OUTPUT: 16¥     |         192000 | False    | 模型调用 Baichuan2-Turbo-192k                                                                                                                                                                                                                                           |
| Baichuan2-53B                | INPUT: 20¥, OUTPUT: 20¥     |          32768 | False    | 模型调用 Baichuan2-53B                                                                                                                                                                                                                                                  |
| chatglm-66b                  | free                        |           8192 | False    | ChatGLM-66B 是智谱AI和清华大学 KEG 实验室联合发布的对话预训练模型。                                                                                                                                                                                                     |
| glm-4-0520                   | INPUT: 100¥, OUTPUT: 100¥   |         128000 | False    | 我们当前的最先进最智能的模型，指令遵从能力大幅提升18.6%，发布于20240605。                                                                                                                                                                                               |
| glm-4                        | INPUT: 100¥, OUTPUT: 100¥   |         128000 | False    | 最新的 GLM-4 、最大支持 128k 上下文、支持 Function Call 、Retreival。                                                                                                                                                                                                   |
| glm-4-air                    | INPUT: 1¥, OUTPUT: 1¥       |         128000 | False    | 性价比最高的版本，综合性能接近GLM-4，速度快，价格实惠。                                                                                                                                                                                                                 |
| glm-4-airx                   | INPUT: 10¥, OUTPUT: 10¥     |         128000 | False    | GLM-4-Air 的高性能版本，效果不变，推理速度达到其2.6倍。                                                                                                                                                                                                                 |
| glm-4-flash                  | INPUT: 0.1¥, OUTPUT: 0.1¥   |         128000 | False    | 适用简单任务，速度最快，价格最实惠的版本。                                                                                                                                                                                                                              |
| glm-3-turbo                  | INPUT: 1¥, OUTPUT: 1¥       |         128000 | False    | 最新的glm-3-turbo、最大支持 128k上下文、支持Function Call、Retreival。                                                                                                                                                                                                  |
| zhipu-embedding-2            | INPUT: 0.5¥, OUTPUT: 0.5¥   |            nan | False    | Embedding是将输入的文本信息进行向量化表示。Embedding适用于搜索、聚类、推荐、异常检测和分类任务等任务。                                                                                                                                                                  |
| deepseek-chat-v2             | INPUT: 1¥, OUTPUT: 2¥       |          32768 | False    | 擅长通用对话任务，上下文长度为 32K。DeepSeek-V2 开源版本支持 128K 上下文，API/网页版本支持 32K 上下文。                                                                                                                                                                 |
| deepseek-coder               | INPUT: 1¥, OUTPUT: 2¥       |          16384 | False    | 擅长处理编程任务，上下文长度为 16K。                                                                                                                                                                                                                                    |
| gemini-pro                   | free                        |            nan | False    |                                                                                                                                                                                                                                                                         |
| abab6.5-chat                 | INPUT: 30¥, OUTPUT: 30¥     |           8192 | False    |                                                                                                                                                                                                                                                                         |
| abab6.5s-chat                | INPUT: 10¥, OUTPUT: 10¥     |         245760 | False    |                                                                                                                                                                                                                                                                         |
| abab6.5g-chat                | INPUT: 5¥, OUTPUT: 5¥       |           8192 | False    |                                                                                                                                                                                                                                                                         |
| abab6-chat                   | INPUT: 100¥, OUTPUT: 100¥   |          32768 | False    |                                                                                                                                                                                                                                                                         |
| abab5.5-chat                 | INPUT: 15¥, OUTPUT: 15¥     |          16384 | False    |                                                                                                                                                                                                                                                                         |
| moonshot-v1-8k               | INPUT: 12¥, OUTPUT: 12¥     |           8192 | False    | 模型调用 moonshot-v1-8k                                                                                                                                                                                                                                                 |
| moonshot-v1-32k              | INPUT: 24¥, OUTPUT: 24¥     |          32768 | False    | 模型调用 moonshot-v1-32k                                                                                                                                                                                                                                                |
| moonshot-v1-128k             | INPUT: 60¥, OUTPUT: 60¥     |         128000 | False    | 模型调用 moonshot-v1-128k                                                                                                                                                                                                                                               |
| gpt-4o                       | INPUT: 5$, OUTPUT: 15$      |         128000 | False    | Our most advanced, multimodal flagship model that’s cheaper and faster than GPT-4 Turbo. Currently points to gpt-4o-2024-05-13.                                                                                                                                         |
| gpt-4o-2024-05-13            | INPUT: 5$, OUTPUT: 15$      |         128000 | False    | gpt-4o currently points to this version.                                                                                                                                                                                                                                |
| gpt-4-turbo                  | INPUT: 10$, OUTPUT: 30$     |         128000 | False    | GPT-4 Turbo with Vision. The latest GPT-4 Turbo model with vision capabilities. Vision requests can now use JSON mode and function calling. Currently points to gpt-4-turbo-2024-04-09.                                                                                 |
| gpt-4-turbo-2024-04-09       | INPUT: 10$, OUTPUT: 30$     |         128000 | False    | GPT-4 Turbo with Vision model. Vision requests can now use JSON mode and function calling. gpt-4-turbo currently points to this version.                                                                                                                                |
| gpt-4-turbo-preview          | INPUT: 10$, OUTPUT: 30$     |         128000 | False    | GPT-4 Turbo preview model. Currently points to gpt-4-0125-preview.                                                                                                                                                                                                      |
| gpt-4-0125-preview           | INPUT: 10$, OUTPUT: 30$     |         128000 | False    | GPT-4 Turbo preview model intended to reduce cases of “laziness” where the model doesn’t complete a task. Returns a maximum of 4,096 output tokens. Learn more.                                                                                                         |
| gpt-4-1106-preview           | INPUT: 10$, OUTPUT: 30$     |         128000 | False    | GPT-4 Turbo preview model featuring improved instruction following, JSON mode, reproducible outputs, parallel function calling, and more. Returns a maximum of 4,096 output tokens. This is a preview model. Learn more.                                                |
| gpt-4-vision-preview         | INPUT: 10$, OUTPUT: 30$     |         128000 | False    | GPT-4 model with the ability to understand images, in addition to all other GPT-4 Turbo capabilities. This is a preview model, we recommend developers to now use gpt-4-turbo which includes vision capabilities. Currently points to gpt-4-1106-vision-preview.        |
| gpt-4-1106-vision-preview    | INPUT: 10$, OUTPUT: 30$     |         128000 | False    | GPT-4 model with the ability to understand images, in addition to all other GPT-4 Turbo capabilities. This is a preview model, we recommend developers to now use gpt-4-turbo which includes vision capabilities. Returns a maximum of 4,096 output tokens. Learn more. |
| gpt-4                        | INPUT: 30$, OUTPUT: 60$     |           8192 | False    | Currently points to gpt-4-0613. See continuous model upgrades.                                                                                                                                                                                                          |
| gpt-4-0613                   | INPUT: 30$, OUTPUT: 60$     |           8192 | False    | Snapshot of gpt-4 from June 13th 2023 with improved function calling support.                                                                                                                                                                                           |
| gpt-3.5-turbo-0125           | INPUT: 0.5$, OUTPUT: 1.5$   |          16385 | False    | The latest GPT-3.5 Turbo model with higher accuracy at responding in requested formats and a fix for a bug which caused a text encoding issue for non-English language function calls. Returns a maximum of 4,096 output tokens. Learn more.                            |
| gpt-3.5-turbo                | INPUT: 0.5$, OUTPUT: 1.5$   |          16385 | False    | Currently points to gpt-3.5-turbo-0125.                                                                                                                                                                                                                                 |
| gpt-3.5-turbo-1106           | INPUT: 0.5$, OUTPUT: 1.5$   |          16385 | False    | GPT-3.5 Turbo model with improved instruction following, JSON mode, reproducible outputs, parallel function calling, and more. Returns a maximum of 4,096 output tokens. Learn more.                                                                                    |
| text-embedding-3-small       | INPUT: 0.02$, OUTPUT: 0.02$ |            nan | False    | Embedding V3 small. Increased performance over 2nd generation ada embedding model                                                                                                                                                                                       |
| text-embedding-3-large       | INPUT: 0.13$, OUTPUT: 0.13$ |            nan | False    | Embedding V3 large. Most capable embedding model for both english and non-english tasks                                                                                                                                                                                 |
| text-embedding-ada-002       | INPUT: 0.1$, OUTPUT: 0.1$   |            nan | False    | Most capable 2nd generation embedding model, replacing 16 first generation models                                                                                                                                                                                       |
| whisper-v3                   | free                        |            nan | True     |                                                                                                                                                                                                                                                                         |
| funasr                       | free                        |            nan | True     |                                                                                                                                                                                                                                                                         |
| baichuan2-7b                 | free                        |           8192 | True     | Baichuan 2 是百川智能推出的新一代开源大语言模型，采用 2.6 万亿 Tokens 的高质量语料训练。                                                                                                                                                                                |
| chatglm3                     | free                        |           8192 | True     | ChatGLM3 是智谱AI和清华大学 KEG 实验室联合发布的对话预训练模型。                                                                                                                                                                                                        |
| chatglm3-32k                 | free                        |          32768 | True     | ChatGLM3 是智谱AI和清华大学 KEG 实验室联合发布的对话预训练模型。                                                                                                                                                                                                        |
| deepseek-coder-6.7b-instruct | free                        |          16384 | True     | Deepseek Coder is composed of a series of code language models, each trained from scratch on 2T tokens, with a composition of 87% code and 13% natural language in both English and Chinese.                                                                            |
| deepseek-coder-6.7b-base     | free                        |          16384 | True     | Deepseek Coder is composed of a series of code language models, each trained from scratch on 2T tokens, with a composition of 87% code and 13% natural language in both English and Chinese.                                                                            |
| m3e                          | free                        |            nan | True     |                                                                                                                                                                                                                                                                         |
| m3e-large                    | free                        |            nan | True     |                                                                                                                                                                                                                                                                         |
| text2vec-large-chinese       | free                        |            nan | True     |                                                                                                                                                                                                                                                                         |
| gte-large-zh                 | free                        |            nan | True     |                                                                                                                                                                                                                                                                         |
| stella-large-zh-v2           | free                        |            nan | True     |                                                                                                                                                                                                                                                                         |
| jina-embeddings-v2-base-zh   | free                        |            nan | True     |                                                                                                                                                                                                                                                                         |
| bge-m3                       | free                        |            nan | True     |                                                                                                                                                                                                                                                                         |
| multilingual-e5-large        | free                        |            nan | True     |                                                                                                                                                                                                                                                                         |
| lingua                       | free                        |           4096 | True     |                                                                                                                                                                                                                                                                         |
| oneke                        | free                        |            nan | True     |                                                                                                                                                                                                                                                                         |
| qwen-14b-chat                | free                        |           8192 | True     |                                                                                                                                                                                                                                                                         |
| bge-reranker-base            | free                        |           8192 | True     |                                                                                                                                                                                                                                                                         |
| bge-reranker-v2-m3           | free                        |           8192 | True     |                                                                                                                                                                                                                                                                         |
| xverse-13b-256k              | free                        |         256000 | True     |                                                                                                                                                                                                                                                                         |
| yi-6b-base                   | free                        |           4096 | True     |                                                                                                                                                                                                                                                                         |
| yi-6b-200k                   | free                        |         200000 | True     |                                                                                                                                                                                                                                                                         |
| yi-6b-chat                   | free                        |           4096 | True     |                                                                                                                                                                                                                                                                         |


# Quick Start 

## OpenAI Client

```python
from openai import OpenAI

client = OpenAI(
    api_key=f"{user_name}:{user_password}",
    base_url="https://modelhub.puyuan.tech/api/v1"
)

client.chat.completions.create(..., model="self-host-models")
```

## ModelhubClient

### Initialization
```python
from modelhub import ModelhubClient

client = ModelhubClient(
    host="https://modelhub.puyuan.tech/api/",
    user_name="xxxx",
    user_password="xxxx",
    model="xxx", # Optional
)
```

### Get supported models

```python
client.supported_models
```

### Create a stateless chat
```python
response = client.chat(
    query,
    model="xxx", # Optional(be None to use the model specific in initialization)
    history=history,
    parameters=dict(
        key1=value1,
        key2=value2
    )
)
```

## Get embeddings

```python
client.get_embeddings(["你好", "Hello"], model="m3e")
```

### Jina Embedding V3

Task-Specific Embedding: Customize embeddings through the task argument with the following options:
- retrieval.query: Used for query embeddings in asymmetric retrieval tasks
- retrieval.passage: Used for passage embeddings in asymmetric retrieval tasks
- separation: Used for embeddings in clustering and re-ranking applications
- classification: Used for embeddings in classification tasks
- text-matching: Used for embeddings in tasks that quantify similarity between two texts, such as STS or symmetric retrieval tasks

```python
client.get_embeddings(["你好", "Hello"], model="jina-embedding-v3", parameters={
    "task_type": "retrieval.query"
})
```

## Context Compression/Distillation

Chat using [lingua](https://github.com/microsoft/LLMLingua) will return a compressed/distillated context. Currently we use `Llama-2-7B-Chat-GPTQ` as LLMlingua backend. Theorically, any local model(Baichuan, ChatGLM, etc.) which can be loaded using `AutoModelForCasualLM` can be used as the backend, thus should provide a `compress` API for every local model, this is a future work since `LLMlingua` doesn't support it naively.

Parameters for `lingua` model:

```python
client.chat(
    prompt: str,
    model = "lingua",
    history: List[Dict[str, str]],
    parameters = dict(
        question: str = "",
        ratio: float = 0.5,
        target_token: float = -1,
        iterative_size: int = 200,
        force_context_ids: List[int] = None,
        force_context_number: int = None,
        use_sentence_level_filter: bool = False,
        use_context_level_filter: bool = True,
        use_token_level_filter: bool = True,
        keep_split: bool = False,
        keep_first_sentence: int = 0,
        keep_last_sentence: int = 0,
        keep_sentence_number: int = 0,
        high_priority_bonus: int = 100,
        context_budget: str = "+100",
        token_budget_ratio: float = 1.4,
        condition_in_question: str = "none",
        reorder_context: str = "original",
        dynamic_context_compression_ratio: float = 0.0,
        condition_compare: bool = False,
        add_instruction: bool = False,
        rank_method: str = "llmlingua",
        concate_question: bool = True,
    )
)
```

## Async Support

Every sync method has the corresponding async one starts with "a"(See [API Documentation](#ModelhubClient) below). For example:

Use async mechanism to make concurrent requests.

**Note** Unlike API models, local models are now single threaded, requested will be queued when using async. In the future, we need to adopt a more flexible inference pipeline. [Github Topic](https://github.com/topics/llm-inference)

```python
import anyio

async with anyio.create_task_group() as tg:
    async def query(question):
        print(await client.achat(question, model="gpt-3.5-turbo"))
    questions = ["hello", "nihao", "test", "test1", "test2"]
    for q in questions:
        tg.start_soon(query, q)
```

### `gemini-pro` embedding need extra parameters

Use the `embed_content` method to generate embeddings. The method handles embedding for the following tasks (`task_type`):

| Task Type           | Description                                                                                                    |
| ------------------- | -------------------------------------------------------------------------------------------------------------- |
| RETRIEVAL_QUERY     | Specifies the given text is a query in a search/retrieval setting.                                             |
| RETRIEVAL_DOCUMENT  | Specifies the given text is a document in a search/retrieval setting. Using this task type requires a `title`. |
| SEMANTIC_SIMILARITY | Specifies the given text will be used for Semantic Textual Similarity (STS).                                   |
| CLASSIFICATION      | Specifies that the embeddings will be used for classification.                                                 |
| CLUSTERING          | Specifies that the embeddings will be used for clustering.                                                     |


## Response

```yaml
generated_text: response_text from model
history: generated history, **only chatglm3 return this currently.**
details: generation details. Include tokens used, request duration, ...
```

## History Parameter

You can either use list of pre-defined message types or raw dicts containing `role` and `content` KV as history.

**Note that not every model support role type like `system`**

```python
# import some pre-defined message types
from modelhub.common.types import SystemMessage, AIMessage, UserMessage
# construct history of your own
history = [
    SystemMessage(content="xxx", other_value="xxxx"),
    UserMessage(content="xxx", other="xxxx"),
]
```


# Examples

## Use ChatCLM3 for tools calling

```python
from modelhub import ModelhubClient, VLMClient
from modelhub.common.types import SystemMessage

client = ModelhubClient(
    host="https://xxxxx/api/",
    user_name="xxxxx",
    user_password="xxxxx",
)
tools = [
    {
        "name": "track",
        "description": "追踪指定股票的实时价格",
        "parameters": {
            "type": "object",
            "properties": {"symbol": {"description": "需要追踪的股票代码"}},
            "required": ["symbol"],
        },
    },
    {
        "name": "text-to-speech",
        "description": "将文本转换为语音",
        "parameters": {
            "type": "object",
            "properties": {
                "text": {"description": "需要转换成语音的文本"},
                "voice": {"description": "要使用的语音类型（男声、女声等）"},
                "speed": {"description": "语音的速度（快、中等、慢等）"},
            },
            "required": ["text"],
        },
    },
]

# construct system history
history = [
    SystemMessage(
        content="Answer the following questions as best as you can. You have access to the following tools:",
        tools=tools,
    )
]
query = "帮我查询股票10111的价格"

# call ChatGLM3
response = client.chat(query, model="ChatGLM3", history=history)
history = response.history
print(response.generated_text)
```
```shell
Output:
{"name": "track", "parameters": {"symbol": "10111"}}
```

```python
# generate a fake result for track function call

result = {"price": 1232}

res = client.chat(
    json.dumps(result),
    parameters=dict(role="observation"), # Tell ChatGLM3 this is a function call result
    model="ChatGLM3",
    history=history,
)
print(res.generated_text)
```

```shell
Output:
根据API调用结果，我得知当前股票的价格为1232。请问您需要我为您做什么？
```
# Contact
