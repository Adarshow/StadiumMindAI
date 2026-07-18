from fastapi import APIRouter, Depends, HTTPException, Request
from slowapi import Limiter
from slowapi.util import get_remote_address
from src.domain.models import StadiumContext, MasterActionPlan
from src.application.orchestration import MasterOrchestrator
from src.application.agents.specialized_agents import (
    CrowdIntelligenceAgent, TransportationAgent, AccessibilityAgent,
    SustainabilityAgent, EmergencyResponseAgent, FanExperienceAgent
)
from src.domain.interfaces import ILLMProvider, IPromptTemplateProvider
from src.config.settings import settings

router = APIRouter(prefix="/api/v1", tags=["Operational Intelligence"])
limiter = Limiter(key_func=get_remote_address)

from src.infrastructure.llm_provider import GoogleGeminiProvider
from src.infrastructure.prompt_provider import FilePromptTemplateProvider

# Dependency Injection
def get_orchestrator() -> MasterOrchestrator:
    llm = GoogleGeminiProvider()
    prompt = FilePromptTemplateProvider()
    
    # In a fully scaled app, you'd instantiate all agents. We'll use a subset to conserve Vercel serverless execution limits.
    agents = [
        CrowdIntelligenceAgent(llm, prompt),
        TransportationAgent(llm, prompt),
        EmergencyResponseAgent(llm, prompt)
    ]
    return MasterOrchestrator(agents, llm, prompt)

@router.post("/process-event", response_model=MasterActionPlan)
@limiter.limit(settings.rate_limit)
async def process_stadium_event(
    request: Request,
    context: StadiumContext,
    orchestrator: MasterOrchestrator = Depends(get_orchestrator)
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
