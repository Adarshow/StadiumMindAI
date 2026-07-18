from abc import ABC, abstractmethod
from typing import Dict, Any
from .models import AgentOutput

class ILLMProvider(ABC):
    @abstractmethod
    async def generate_structured_response(self, prompt: str, schema: Any) -> Any:
        """
        Generates a structured response from the LLM based on a Pydantic schema.
        """
        pass

class IPromptTemplateProvider(ABC):
    @abstractmethod
    def get_template(self, template_name: str) -> str:
        """
        Retrieves a prompt template by name.
        """
        pass
