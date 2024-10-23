import os
from typing import Optional, Literal

from langchain_anthropic import ChatAnthropic
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_voyageai import VoyageAIEmbeddings

class MIRACLEModelFactory:
    @staticmethod
    def get_anthropic_model(
        model_name: Literal["haiku", "sonnet", "opus"] = "sonnet",
        temperature: float = 0.1,
        max_tokens: int = 4096,
        max_retries: int =3,
        timeout: Optional[float] = None,
    ) -> ChatAnthropic:
        """Load the Anthropic model easily. You can freely revise it to make it easier to use."""

        model_mapping = {
            "sonnet": "claude-3-5-sonnet-20241022",
            "haiku": "claude-3-haiku-20240307",
            "opus": "claude-3-opus-latest"
        }

        return ChatAnthropic(
            model=model_mapping[model_name],
            temperature=temperature,
            max_tokens=max_tokens,
            anthropic_api_key=os.getenv('ANTHROPIC_API_KEY'),
            timeout=timeout,
            max_retries=max_retries,
            extra_headers={"anthropic-beta": "prompt-caching-2024-07-31"}
        )

    @staticmethod
    def get_openai_model(
        model_name: Literal['gpt-4o-mini', 'gpt-4o', 'chatgpt-4o-latest'] = "gpt-4o",
        temperature: float = 0.1,
        max_tokens: int = 4096,
        max_retries: int = 3
    ) -> ChatOpenAI:
        model_mapping = {
            "gpt-4o-mini": "gpt-4o-mini-2024-07-18",
            "gpt-4o": "gpt-4o-2024-08-06",
            "chatgpt-4o-latest": "chatgpt-4o-latest"
        }

        return ChatOpenAI(
            model_name=model_mapping[model_name],
            temperature=temperature,
            max_tokens=max_tokens,
            max_retries=max_retries,
            openai_api_key=os.getenv('OPENAI_API_KEY'),
        )

    @staticmethod
    def get_openai_embedding_model(
        model_name: Literal['small', 'large'] = 'small'
    ) -> OpenAIEmbeddings:
        """Load the OpenAI embedding model easily. You can freely revise it to make it easier to use."""
        model_mapping = {
            "small": "text-embedding-3-small",
            "large": "text-embedding-3-large"
        }
        return OpenAIEmbeddings(
            model=model_mapping[model_name],
            openai_api_key=os.getenv('OPENAI_API_KEY')
        )

    @staticmethod
    def get_voyage_embedding_model(
        model_name: Literal["voyage-3", "voyage-3-lite", "voyage-finance-2", "voyage-multilingual-2", "voyage-code-2"] = "voyage-3"
    ) -> VoyageAIEmbeddings:
        return VoyageAIEmbeddings(
            model=model_name,
            voyage_api_key=os.getenv('VOYAGE_API_KEY')
        )

