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
def mock_llm_provider():
    provider = AsyncMock()
    provider.generate_structured_response.return_value = MasterActionPlan(
        synthesis_reasoning="Mock reasoning",
        prioritized_actions=[],
        overall_confidence=0.9
    )
    return provider

@pytest.fixture
def mock_prompt_provider():
    provider = MagicMock()
    provider.get_template.return_value = "Mock template with {{context}} and {{agent_outputs}}"
    return provider

@pytest.mark.asyncio
async def test_orchestrator_handles_agent_failures_gracefully(mock_context, mock_llm_provider, mock_prompt_provider):
    # Setup two mock agents. One succeeds, one raises an exception.
    successful_agent = AsyncMock(spec=BaseAgent)
    successful_agent.name = "Successful Agent"
    successful_agent.analyze.return_value = AgentOutput(
        agent_name="Successful Agent",
        observations=[], risks=[], recommended_actions=[], reasoning="Success", confidence=1.0
    )
    
    failing_agent = AsyncMock(spec=BaseAgent)
    failing_agent.name = "Failing Agent"
    failing_agent.analyze.side_effect = Exception("Simulated API Timeout")
    
    agents = [successful_agent, failing_agent]
    
    orchestrator = MasterOrchestrator(agents, mock_llm_provider, mock_prompt_provider)
    
    # Execution
    master_plan = await orchestrator.process_context(mock_context)
    
    # Assertions
    assert master_plan is not None
    assert master_plan.overall_confidence == 0.9
    # Ensure the LLM provider was only called once, despite one agent failing
    mock_llm_provider.generate_structured_response.assert_called_once()

    # The prompt sent to the LLM should contain the successful agent's output
    call_args = mock_llm_provider.generate_structured_response.call_args[0]
    prompt_sent = call_args[0]
    assert "Successful Agent" in prompt_sent
    # The failing agent output shouldn't be there because it raised an exception handled by gather(return_exceptions=True)
    assert "Failing Agent" not in prompt_sent
