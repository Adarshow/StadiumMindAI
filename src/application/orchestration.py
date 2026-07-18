import asyncio
from typing import List
from src.domain.models import StadiumContext, AgentOutput, MasterActionPlan
from src.domain.interfaces import ILLMProvider, IPromptTemplateProvider
from src.application.agents.base_agent import BaseAgent

class MasterOrchestrator:
    """
    The central operational intelligence node.
    
    This class orchestrates a suite of specialized multi-agent systems concurrently,
    synthesizing their independent analyses into a cohesive, prioritized Master Action Plan.
    """
    def __init__(self, agents: List[BaseAgent], llm_provider: ILLMProvider, prompt_provider: IPromptTemplateProvider):
        self.agents = agents
        self.llm_provider = llm_provider
        self.prompt_provider = prompt_provider
        
    async def process_context(self, context: StadiumContext) -> MasterActionPlan:
        """
        Executes the concurrent multi-agent reasoning pipeline against a real-time StadiumContext.
        """
        # Run all specialized agents concurrently, capturing exceptions with a strict timeout
        # Vercel Hobby tier times out at 10s. We enforce 8.0s here to gracefully degrade instead of 504 Gateway Timeout.
        agent_tasks = [agent.analyze(context) for agent in self.agents]
        
        import logging
        logger = logging.getLogger(__name__)
        
        try:
            results = await asyncio.wait_for(
                asyncio.gather(*agent_tasks, return_exceptions=True),
                timeout=8.0
            )
        except asyncio.TimeoutError:
            logger.error("Critical: LLM Agents timed out after 8.0 seconds. Forcing graceful degradation.")
            results = [Exception("Agent execution timed out")] * len(self.agents)
        
        # Filter successful outputs and log/handle failures
        agent_outputs: List[AgentOutput] = []
        for result, agent in zip(results, self.agents):
            if isinstance(result, Exception):
                logger.warning(f"Agent execution failure: {agent.name} failed with error: {str(result)}")
            else:
                agent_outputs.append(result)
        
        # Synthesize with Master Agent prompt
        template = self.prompt_provider.get_template("master_decision.txt")
        
        outputs_json = "\n\n".join([output.model_dump_json(indent=2) for output in agent_outputs])
        context_json = context.model_dump_json(indent=2)
        
        prompt = template.replace("{{context}}", context_json).replace("{{agent_outputs}}", outputs_json)
        
        # Enforce multilingual assistance
        prompt += f"\n\nCRITICAL MULTILINGUAL INSTRUCTION: You MUST write your synthesis_reasoning and all action descriptions strictly in {context.operator_language}. Do not output English unless {context.operator_language} is English."
        
        master_plan: MasterActionPlan = await self.llm_provider.generate_structured_response(prompt, MasterActionPlan)
        return master_plan
