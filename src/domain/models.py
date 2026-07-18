from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any

class StadiumContext(BaseModel):
    timestamp: str = Field(..., description="Current timestamp of the context")
    active_events: List[str] = Field(default_factory=list, description="List of active events or incidents")
    weather: str = Field(..., description="Current weather conditions")
    attendance: int = Field(..., description="Current stadium attendance")
    metrics: Dict[str, Any] = Field(default_factory=dict, description="Key metrics like density, transport status, etc.")
    operator_language: str = Field(default="English", description="The native language of the stadium operator requesting the plan")

class AgentObservation(BaseModel):
    description: str = Field(..., description="Observation made by the agent based on context")
    severity: str = Field(..., description="Severity of the observation: low, medium, high")

class RiskAssessment(BaseModel):
    risk_factor: str = Field(..., description="Identified risk factor")
    probability: float = Field(..., description="Probability of risk occurring (0.0 to 1.0)")
    potential_impact: str = Field(..., description="Potential impact if risk materializes")

class RecommendedAction(BaseModel):
    action_id: str = Field(..., description="Unique identifier for the action")
    description: str = Field(..., description="Detailed description of the recommended action")
    priority: str = Field(..., description="Priority: low, medium, high, critical")
    target_zone: str = Field(..., description="Stadium zone or sector affected")

class AgentOutput(BaseModel):
    agent_name: str = Field(..., description="Name of the agent generating the output")
    observations: List[AgentObservation] = Field(default_factory=list)
    risks: List[RiskAssessment] = Field(default_factory=list)
    recommended_actions: List[RecommendedAction] = Field(default_factory=list)
    reasoning: str = Field(..., description="Detailed explanation of the agent's reasoning")
    confidence: float = Field(..., description="Agent's confidence in its output (0.0 to 1.0)")

class PrioritizedAction(BaseModel):
    action: RecommendedAction
    source_agent: str
    execution_order: int

class MasterActionPlan(BaseModel):
    synthesis_reasoning: str = Field(..., description="Master agent's synthesis of all specialized agent outputs")
    prioritized_actions: List[PrioritizedAction] = Field(default_factory=list)
    overall_confidence: float = Field(..., description="Master agent's confidence in the final plan")
