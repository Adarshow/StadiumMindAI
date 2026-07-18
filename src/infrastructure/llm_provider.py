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
            # The Gemini API does not natively support nested Pydantic models with $defs/$ref in response_schema.
            # We inject the JSON schema directly into the prompt to guarantee structure.
            schema_json = schema.model_json_schema()
            full_prompt = f"{prompt}\n\nCRITICAL: You MUST return a raw JSON object that strictly adheres to the following JSON schema. Do not include markdown formatting like ```json:\n{json.dumps(schema_json)}"

            response = self.client.models.generate_content(
                model=self.model_name,
                contents=full_prompt,
                config={
                    'response_mime_type': 'application/json',
                    'temperature': 0.2, # Low temperature for more deterministic reasoning
                },
            )
            
            # Clean potential markdown blocks if Gemini ignores instructions
            text = response.text.strip()
            if text.startswith("```json"):
                text = text.replace("```json", "").replace("```", "").strip()
            elif text.startswith("```"):
                text = text.replace("```", "").strip()

            return schema.model_validate_json(text)
        except Exception as e:
            # Re-raise the exception so the MasterOrchestrator can catch it
            print(f"Gemini API Error: {e}")
            raise e
