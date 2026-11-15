from openai import OpenAI

from src.domain.llm_sdk import LLMSdk


class OpenAICaller(LLMSdk):
    def __init__(self) -> None:
        self.client = OpenAI()

    def chat(
        self, model_name: str, messages: list[dict], max_tokens: int = 256
    ) -> None:
        response = self.client.chat.completions.create(
            model=model_name, max_completion_tokens=max_tokens, messages=messages
        )

        # La respuesta llega dentro de una lista de opciones (choices); usamos la primera.
        eleccion = response.choices[0]
        print(eleccion.message.content or "(respuesta vacía)")

        # Por qué terminó: "stop" = de forma natural; "length" = se cortó por el límite.
        print(f"\n[fin] {eleccion.finish_reason}")
        print(
            f"[tokens] entrada={response.usage.prompt_tokens} "
            f"salida={response.usage.completion_tokens}"
        )
