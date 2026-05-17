"""
https://github.com/abetlen/llama-cpp-python
"""

from llama_cpp import Llama, ChatCompletionRequestSystemMessage, ChatCompletionRequestUserMessage
from pathlib import Path


class LocalLLM:
    DEFAULT_MODEL_PATH = 'Llama-3.2-3B-Instruct-Q4_K_M.gguf'
    CONTENT = ('Ты голосовой ассистент женского рода. Отвечай кратко, естественно и дружелюбно. '
               'Твои ответы будут преобразованы в речь, поэтому избегай маркированных списков, сложных символов и длинных предложений'
               'Общайся только на русском языке. Если встречаются английские слова всё равно пиши их по русски')

    def __init__(self, model_path: str = DEFAULT_MODEL_PATH):
        if not Path(model_path).exists():
            raise FileNotFoundError(f"Model not found: {model_path}")

        self.llm = Llama(
            model_path=model_path,
            chat_format="chatml",
            logits_all=False,
        )

        self.messages: list = [  # Нестрогая типизация
            ChatCompletionRequestSystemMessage(
                role="system",
                content=self.CONTENT
            )
        ]

    def get_response(self, user_message: str) -> str:

        user_msg = ChatCompletionRequestUserMessage(
            role="user",
            content=user_message
        )

        self.messages.append(user_msg)

        output = self.llm.create_chat_completion(
            messages=self.messages,
            temperature=0.7,
            max_tokens=150
        )
        return output['choices'][0]['message']['content']
