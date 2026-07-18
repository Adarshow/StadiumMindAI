import pytest
import asyncio
from unittest.mock import AsyncMock, MagicMock
from src.domain.models import StadiumContext, MasterActionPlan, AgentOutput
from src.application.orchestration import MasterOrchestrator
from src.application.agents.base_agent import BaseAgent

@pytest.fixture
def mock_context():
    return StadiumContext(
        timestamp="14:00 PM",
        active_events=[],
        weather="Sunny",
        attendance=65000,
        metrics={"density": "high"}
    )

@pytest.fixture
def mock_prompt_provider():
    provider = MagicMock()
    provider.get_template.return_value = "Mock template with {{context}} and {{agent_outputs}}"
    return provider

@pytest.mark.asyncio
async def test_orchestrator_handles_agent_failures_gracefully(mock_context, mock_prompt_provider):
    # Setup LLM Provider for Master Agent
    master_llm_provider = AsyncMock()
    master_llm_provider.generate_structured_response.return_value = MasterActionPlan(
        synthesis_reasoning="Mock reasoning",
        prioritized_actions=[],
        overall_confidence=0.9
    )

    # Setup Successful Agent
    successful_llm_provider = AsyncMock()
    successful_llm_provider.generate_structured_response.return_value = AgentOutput(
        agent_name="Successful Agent",
        observations=[], risks=[], recommended_actions=[], reasoning="Success", confidence=1.0
    )
    successful_agent = BaseAgent("Successful Agent", successful_llm_provider, mock_prompt_provider)
    
    # Setup Failing Agent
    failing_llm_provider = AsyncMock()
    failing_llm_provider.generate_structured_response.side_effect = Exception("Simulated API Timeout")
    failing_agent = BaseAgent("Failing Agent", failing_llm_provider, mock_prompt_provider)
    
    agents = [successful_agent, failing_agent]
    
    orchestrator = MasterOrchestrator(agents, master_llm_provider, mock_prompt_provider)
    
    # Execution
    master_plan = await orchestrator.process_context(mock_context)
    
    # Assertions
    assert master_plan is not None
    assert master_plan.overall_confidence == 0.9
    
    # Ensure the master LLM provider was called once
    master_llm_provider.generate_structured_response.assert_called_once()

    # The prompt sent to the master LLM should contain BOTH agents because the failing one returns a fallback
    call_args = master_llm_provider.generate_structured_response.call_args[0]
    prompt_sent = call_args[0]
    
    assert "Successful Agent" in prompt_sent
    assert "Failing Agent" in prompt_sent
    assert "Agent failed to process context" in prompt_sent  # Verify the fallback text was included
