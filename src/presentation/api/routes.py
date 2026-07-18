from fastapi import APIRouter, Depends, HTTPException
from src.domain.models import StadiumContext, MasterActionPlan
from src.application.orchestration import MasterOrchestrator
from src.application.agents.specialized_agents import (
    CrowdIntelligenceAgent, TransportationAgent, AccessibilityAgent,
    SustainabilityAgent, EmergencyResponseAgent, FanExperienceAgent
)
from src.domain.interfaces import ILLMProvider, IPromptTemplateProvider

router = APIRouter(prefix="/api/v1", tags=["Operational Intelligence"])

# Mock Dependency Injection for the sake of the structural blueprint
def get_mock_orchestrator() -> MasterOrchestrator:
    # In a real app, these would be proper concrete classes injected via a DI container
    class DummyLLM(ILLMProvider):
        async def generate_structured_response(self, prompt, schema):
            return schema(synthesis_reasoning="Mocked fallback", prioritized_actions=[], overall_confidence=0.5)

    class DummyPrompt(IPromptTemplateProvider):
        def get_template(self, name): return "Mock Template"

    llm = DummyLLM()
    prompt = DummyPrompt()
    agents = [
        CrowdIntelligenceAgent(llm, prompt),
        TransportationAgent(llm, prompt)
    ]
    return MasterOrchestrator(agents, llm, prompt)

@router.post("/process-event", response_model=MasterActionPlan)
async def process_stadium_event(
    context: StadiumContext,
    orchestrator: MasterOrchestrator = Depends(get_mock_orchestrator)
):
    """
    Ingests a live stadium context event and triggers the multi-agent reasoning pipeline
    to synthesize a preemptive action plan.
    """
    try:
        plan = await orchestrator.process_context(context)
        return plan
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
