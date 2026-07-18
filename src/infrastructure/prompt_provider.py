import os
from src.domain.interfaces import IPromptTemplateProvider

class FilePromptTemplateProvider(IPromptTemplateProvider):
    def __init__(self, base_dir: str = None):
        if base_dir is None:
            # Default to src/infrastructure/prompts relative to project root
            self.base_dir = os.path.join(os.path.dirname(__file__), "prompts")
        else:
            self.base_dir = base_dir

    def get_template(self, template_name: str) -> str:
        filepath = os.path.join(self.base_dir, template_name)
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            # Fallback to a generic template if file is missing (to support the competition mock setup)
            if template_name == "master_decision.txt":
                return "You are the Master AI Orchestrator. Synthesize the following agent outputs into a unified action plan based on the given context.\n\nContext:\n{{context}}\n\nAgent Outputs:\n{{agent_outputs}}"
            else:
                return "You are a specialized AI agent. Analyze the following stadium context and provide your observations, risk assessments, and recommended actions.\n\nContext:\n{{context}}"
