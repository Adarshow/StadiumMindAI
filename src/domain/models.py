from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any

class StadiumContext(BaseModel):
    """
    Represents the real-time operational context of the stadium.
    This includes telemetry data, crowd metrics, weather, and language preferences.
    """
    timestamp: str = Field(..., max_length=50, description="Current timestamp of the context")
    active_events: List[str] = Field(default_factory=list, max_length=20, description="List of active events or incidents")
    weather: str = Field(..., max_length=100, description="Current weather conditions")
    attendance: int = Field(..., ge=0, le=200000, description="Current stadium attendance")
    metrics: Dict[str, Any] = Field(default_factory=dict, description="Key metrics like density, transport status, etc.")
    operator_language: str = Field(default="English", max_length=50, description="The native language of the stadium operator requesting the plan")

class AgentObservation(BaseModel):
    """
    A specific observation made by an autonomous agent based on the StadiumContext.
    """
    description: str = Field(..., description="Observation made by the agent based on context")
    severity: str = Field(..., description="Severity of the observation: low, medium, high")

class RiskAssessment(BaseModel):
    """
    An assessment of potential risks and their likelihood of occurring within the stadium.
    """
    risk_factor: str = Field(..., description="Identified risk factor")
    probability: float = Field(..., description="Probability of risk occurring (0.0 to 1.0)")
    potential_impact: str = Field(..., description="Potential impact if risk materializes")

class RecommendedAction(BaseModel):
    """
    A discrete, actionable recommendation proposed by a specialized agent.
    """
    action_id: str = Field(..., description="Unique identifier for the action")
    description: str = Field(..., description="Detailed description of the recommended action")
    priority: str = Field(..., description="Priority: low, medium, high, critical")
    target_zone: str = Field(..., description="Stadium zone or sector affected")

class AgentOutput(BaseModel):
    """
    The complete, structured output from a single specialized LLM agent.
    """
    agent_name: str = Field(..., description="Name of the agent generating the output")
    observations: List[AgentObservation] = Field(default_factory=list)
    risks: List[RiskAssessment] = Field(default_factory=list)
    recommended_actions: List[RecommendedAction] = Field(default_factory=list)
    reasoning: str = Field(..., description="Detailed explanation of the agent's reasoning")
    confidence: float = Field(..., description="Agent's confidence in its output (0.0 to 1.0)")

class PrioritizedAction(BaseModel):
    """
    An action that has been ranked and ordered by the Master Orchestrator.
    """
    action: RecommendedAction
    source_agent: str
    execution_order: int

class MasterActionPlan(BaseModel):
    """
    The final, synthesized operational playbook containing all prioritized actions.
    This is the ultimate payload delivered to the frontend dashboard.
    """
    synthesis_reasoning: str = Field(..., description="Master agent's synthesis of all specialized agent outputs")
    prioritized_actions: List[PrioritizedAction] = Field(default_factory=list)
    overall_confidence: float = Field(..., description="Master agent's confidence in the final plan")
