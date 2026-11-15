from src.domain.llm_sdk import LLMSdk


class Chatter:
    def __init__(self, model_name: str, llm_sdk: LLMSdk, max_tokens: int = 256) -> None:
        self.model_name = model_name
        self.llm = llm_sdk
        self.max_tokens = max_tokens

    def send_message(self, messages: list[dict]) -> None:
        self.llm.chat(
            model_name=self.model_name, messages=messages, max_tokens=self.max_tokens
        )
