import argparse
import os
import sys

from dotenv import load_dotenv

import src.application.llm_message_builder as LLMMessageBuilder
from src.application.chatter import Chatter
from src.infrastructure.openai import OpenAICaller

load_dotenv()
MODEL = os.getenv("MODEL_NAME")

system_prompt_message_factory = {
    "abstract": "Resume textos. Devuelve exactamente 3 puntos clave, concisos, en español.",
    "classificate": "Clasifica tickets. Devuelve una clasificación del ticket en función de su prioridad: 'low', 'middle', 'high'. Sólo devuelve 1 palabra con la clasificación",
    "extract": "Extrae nombres. Extrae todo los nombres de un texto.",
}


def send_messages(messages: list[dict[str, str]]):
    llm_sdk = OpenAICaller()
    chatter = Chatter(model_name=MODEL, llm_sdk=llm_sdk, max_tokens=255)

    chatter.send_message(messages=messages)


def read_stdin(param: str):
    return sys.stdin(param)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Usa un modelo para generar resumen, clasificación o extraer partes de un texto"
    )

    parser.add_argument(
        "message",
        default=None,
        nargs="?",
        type=str,
        help="Puedes pasar el mensaje de texto entre comillas o usando f para usar stdin: f < path/file.txt",
    )

    parser.add_argument(
        "-o",
        "--operation",
        type=str,
        choices=["abstract", "classificate", "extract"],
        default="abstract",
        required=False,
        help="Operación que realiza el modelo con el texto",
    )

    args = parser.parse_args()

    if args.message is None:
        parser.parse_args(["--help"])

    if args.message == "f":
        text = sys.stdin.read()
    else:
        text = args.message

    messages = []
    message_system_prompt = system_prompt_message_factory.get(args.operation)
    messages.append(LLMMessageBuilder.build(message_system_prompt, "system"))
    messages.append(LLMMessageBuilder.build(text, "user"))

    send_messages(messages=messages)
