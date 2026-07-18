import json
from src.domain.interfaces import ILLMProvider, IPromptTemplateProvider
from src.domain.models import StadiumContext, AgentOutput

class BaseAgent:
    """
    Abstract base class for all specialized LLM reasoning agents.
    Provides standardized methods for prompt injection and LLM execution.
    """
    def __init__(self, name: str, llm_provider: ILLMProvider, prompt_provider: IPromptTemplateProvider):
        """
        Initializes the agent with its dependencies.
        """
        self.name = name
        self.llm_provider = llm_provider
        self.prompt_provider = prompt_provider
        self.prompt_template_name = f"{name.lower().replace(' ', '_')}.txt"

    async def analyze(self, context: StadiumContext) -> AgentOutput:
        """
        Executes the agent's domain-specific reasoning against the provided context.
        Returns a structured AgentOutput or a graceful degradation fallback on failure.
        """
        template = self.prompt_provider.get_template(self.prompt_template_name)
        
        # Inject context into prompt
        prompt = template.replace("{{context}}", context.model_dump_json(indent=2))
        
        try:
            # Call LLM provider to get structured output conforming to AgentOutput
            result = await self.llm_provider.generate_structured_response(prompt, AgentOutput)
            result.agent_name = self.name
            return result
        except Exception as e:
            # Graceful degradation fallback
            return AgentOutput(
                agent_name=self.name,
                observations=[{"description": f"Agent failed to process context: {str(e)}", "severity": "high"}],
                risks=[],
                recommended_actions=[],
                reasoning="Agent execution failed. Returning safe fallback.",
                confidence=0.0
            )
