from llama_index.core.llms import ChatMessage

from backend.llm.llm_factory import get_llm


def chat_qa(provider: str, model: str, chat_history: list) -> str:
    llm = get_llm(provider, model)
    messages = [
        ChatMessage(role=msg["role"], content=msg["content"]) for msg in chat_history
    ]
    response = llm.chat(messages)
    return response.message.content
