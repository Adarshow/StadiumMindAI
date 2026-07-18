import json
from google import genai
from typing import Any
from src.domain.interfaces import ILLMProvider
from src.config.settings import settings

class GoogleGeminiProvider(ILLMProvider):
    def __init__(self):
        # The client will use the llm_api_key from settings
        self.client = genai.Client(api_key=settings.llm_api_key)
        self.model_name = "gemini-2.5-flash"

    async def generate_structured_response(self, prompt: str, schema: Any) -> Any:
        try:
            response = self.client.models.generate_content(
                model=self.model_name,
                contents=prompt,
                config={
                    'response_mime_type': 'application/json',
                    'response_schema': schema,
                    'temperature': 0.2, # Low temperature for more deterministic reasoning
                },
            )
            # The response.text is guaranteed to be a JSON string matching the Pydantic schema
            return schema.model_validate_json(response.text)
        except Exception as e:
            # Re-raise the exception so the MasterOrchestrator can catch it
            print(f"Gemini API Error: {e}")
            raise e
