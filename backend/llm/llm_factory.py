from llama_index.llms.ollama import Ollama

LLM_BY_PROVIDER = {
    "ollama": Ollama,
}

# cache
_current_key = None
_current_llm = None


def get_llm(provider: str, model: str):
    """
    Get LLM instance based on provider and model.

    Args:
        provider (str): The LLM provider name.
        model (str): The model name.

    Returns:
        An instance of the corresponding LLM class.
    """
    global _current_key, _current_llm
    key = (provider, model)

    if _current_key == key and _current_llm is not None:
        return _current_llm

    # Build a new instance and replace the cache
    if provider not in LLM_BY_PROVIDER:
        raise ValueError(f"Unsupported provider: {provider}")

    _current_llm = LLM_BY_PROVIDER[provider](model=model)
    _current_key = key
    return _current_llm


def reset_llm_cache():
    """Reset the cached LLM instance."""
    global _current_key, _current_llm
    _current_key = None
    _current_llm = None
