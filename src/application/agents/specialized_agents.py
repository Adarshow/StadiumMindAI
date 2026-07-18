from .base_agent import BaseAgent
from src.domain.interfaces import ILLMProvider, IPromptTemplateProvider

class CrowdIntelligenceAgent(BaseAgent):
    def __init__(self, llm_provider: ILLMProvider, prompt_provider: IPromptTemplateProvider):
        super().__init__("Crowd Intelligence", llm_provider, prompt_provider)

class TransportationAgent(BaseAgent):
    def __init__(self, llm_provider: ILLMProvider, prompt_provider: IPromptTemplateProvider):
        super().__init__("Transportation", llm_provider, prompt_provider)

class AccessibilityAgent(BaseAgent):
    def __init__(self, llm_provider: ILLMProvider, prompt_provider: IPromptTemplateProvider):
        super().__init__("Accessibility", llm_provider, prompt_provider)

class SustainabilityAgent(BaseAgent):
    def __init__(self, llm_provider: ILLMProvider, prompt_provider: IPromptTemplateProvider):
        super().__init__("Sustainability", llm_provider, prompt_provider)

class EmergencyResponseAgent(BaseAgent):
    def __init__(self, llm_provider: ILLMProvider, prompt_provider: IPromptTemplateProvider):
        super().__init__("Emergency Response", llm_provider, prompt_provider)

class FanExperienceAgent(BaseAgent):
    def __init__(self, llm_provider: ILLMProvider, prompt_provider: IPromptTemplateProvider):
        super().__init__("Fan Experience", llm_provider, prompt_provider)
