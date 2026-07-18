import pytest
from unittest.mock import AsyncMock, MagicMock
from src.application.agents.base_agent import BaseAgent
from src.domain.models import StadiumContext

@pytest.fixture
def mock_context():
    return StadiumContext(
        timestamp="14:00 PM",
        active_events=["Test Event"],
        weather="Sunny",
        attendance=50000,
        metrics={},
        operator_language="English"
    )

@pytest.fixture
def mock_prompt_provider():
    provider = MagicMock()
    provider.get_template.return_value = "Mock template"
    return provider

@pytest.mark.asyncio
async def test_agent_graceful_degradation(mock_context, mock_prompt_provider):
    """
    Test that an agent gracefully degrades and returns a fallback AgentOutput 
    when the underlying LLM provider raises an Exception.
    """
    failing_llm_provider = AsyncMock()
    failing_llm_provider.generate_structured_response.side_effect = Exception("API Timeout")
    
    agent = BaseAgent("Test Agent", failing_llm_provider, mock_prompt_provider)
    output = await agent.analyze(mock_context)
    
    # Assertions for graceful degradation
    assert output is not None
    assert output.agent_name == "Test Agent"
    assert output.confidence == 0.0
    assert "Agent execution failed" in output.reasoning
    assert len(output.observations) == 1
    assert output.observations[0].severity == "high"
