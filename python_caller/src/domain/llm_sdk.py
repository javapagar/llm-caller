from abc import ABC, abstractmethod


class LLMSdk(ABC):
    @abstractmethod
    def chat(self, model_name: str, messages: list[dict], max_tokens: int) -> None: ...
