import asyncio
from typing import List
from src.domain.models import StadiumContext, AgentOutput, MasterActionPlan
from src.domain.interfaces import ILLMProvider, IPromptTemplateProvider
from src.application.agents.base_agent import BaseAgent

class MasterOrchestrator:
    def __init__(self, agents: List[BaseAgent], llm_provider: ILLMProvider, prompt_provider: IPromptTemplateProvider):
        self.agents = agents
        self.llm_provider = llm_provider
        self.prompt_provider = prompt_provider
        
    async def process_context(self, context: StadiumContext) -> MasterActionPlan:
        # Run all specialized agents concurrently, capturing exceptions
        agent_tasks = [agent.analyze(context) for agent in self.agents]
        results = await asyncio.gather(*agent_tasks, return_exceptions=True)
        
        # Filter successful outputs and log/handle failures
        agent_outputs: List[AgentOutput] = []
        for result, agent in zip(results, self.agents):
            if isinstance(result, Exception):
                # In production, use structlog to log the exception here
                print(f"Warning: {agent.name} failed with error: {str(result)}")
            else:
                agent_outputs.append(result)
        
        # Synthesize with Master Agent prompt
        template = self.prompt_provider.get_template("master_decision.txt")
        
        outputs_json = "\n\n".join([output.model_dump_json(indent=2) for output in agent_outputs])
        context_json = context.model_dump_json(indent=2)
        
        prompt = template.replace("{{context}}", context_json).replace("{{agent_outputs}}", outputs_json)
        
        master_plan: MasterActionPlan = await self.llm_provider.generate_structured_response(prompt, MasterActionPlan)
        return master_plan
