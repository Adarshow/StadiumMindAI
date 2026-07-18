# StadiumMind AI

**FIFA World Cup 2026 Operational Intelligence Copilot**

## Problem Statement
Managing a global mega-event like the FIFA World Cup involves coordinating massive crowds, sprawling transportation networks, and critical emergency services in real-time. Traditional command centers rely on reactive dashboards and human operators trying to correlate thousands of disjointed data points. This often leads to delayed responses to bottlenecks, sub-optimal resource allocation, and compromised fan experiences.

## Why This Solution is Unique
StadiumMind AI moves beyond simple chatbots and reactive dashboards. It employs a **Proactive Multi-Agent Reasoning Architecture**. By ingesting a simulated stream of real-time stadium metrics, a Master Orchestrator delegates context to specialized AI agents (Crowd, Transport, Accessibility, etc.). These agents don't just report data—they *reason* over it, predicting issues before they occur and recommending prioritized, explainable operational actions.

## Architecture Diagram
```mermaid
graph TD
    A[Event Stream / IoT Sensors] --> B(Master Orchestrator Agent)
    B --> C[Crowd Intelligence Agent]
    B --> D[Transportation Agent]
    B --> E[Accessibility Agent]
    B --> F[Sustainability Agent]
    B --> G[Emergency Response Agent]
    
    C --> H{Synthesis Engine}
    D --> H
    E --> H
    F --> H
    G --> H
    
    H --> I[Master Action Plan]
    I --> J[React + Tailwind UI Command Center]
```

## AI Agent Workflow
1. **Context Ingestion**: Real-time metrics (attendance, weather, shuttle schedules) are passed to the Master Orchestrator.
2. **Concurrent Delegation**: The orchestrator triggers specialized agents using `asyncio.gather`.
3. **Domain-Specific Reasoning**: Each agent assesses risks, correlates data, and generates structured observations with confidence scores.
4. **Synthesis**: The Orchestrator resolves conflicts (e.g., Crowd agent wants to open Gate A, but Transport agent notes Gate A road is blocked) and finalizes the plan.
5. **Execution UI**: The plan is presented to the human operator with an explainability panel.

## Folder Structure
```text
stadium_mind_ai/
├── frontend/                   # React + TypeScript + Tailwind SPA
│   ├── src/components/         # Dashboard UI (Digital Twin, Incident Center, etc.)
│   └── tailwind.config.js
├── src/
│   ├── domain/                 # Core Pydantic Models and Interfaces
│   ├── application/            # Orchestrator and Base Agent logic
│   ├── infrastructure/         # Prompt templates and LLM bindings
│   │   └── prompts/            # Decoupled agent system prompts
│   └── presentation/           # FastAPI application (pending completion)
├── tests/
└── README.md
```

## Installation
### Prerequisites
- Node.js (v18+)
- Python (3.10+)

```bash
# Clone the repository
git clone https://github.com/your-org/stadium-mind-ai.git
cd stadium-mind-ai

# Frontend Setup
cd frontend
npm install

# Backend Setup (Python)
cd ../
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Running Locally
**Start the Frontend Development Server:**
```bash
cd frontend
npm run dev
```
Navigate to `http://localhost:5173` to view the command center. (Note: Ensure the backend is running to receive live simulated data).

## Prompt Engineering Approach
We decoupled prompts from the application code by storing them in `src/infrastructure/prompts/`. 
- **Role-Based Persona**: Each agent is given a strict operational persona (e.g., "You are the Transportation Agent").
- **Structured Context Injection**: Data is injected dynamically via standard string replacements.
- **Strict Output Schema**: The LLM is instructed (and enforced via Pydantic models) to return observations, risks, and recommended actions with explicit confidence scores (0.0 - 1.0).

## Security Considerations
- **API Key Management**: LLM API keys are managed securely via `pydantic-settings` and `.env` files.
- **Data Anonymization**: The simulated event stream assumes all fan data (e.g., CCTV feeds) is anonymized at the edge device level before reaching the AI.
- **Human-in-the-Loop**: The AI makes *recommendations*, not autonomous actuations. Critical actions require human operator sign-off.

## Accessibility Considerations
- **Software Accessibility (WCAG)**: The React dashboard uses high-contrast colors, semantic HTML, and screen-reader-friendly UI patterns.
- **Physical Stadium Accessibility**: The dedicated `AccessibilityAgent` proactively monitors sensory room availability, wheelchair requests, and ADA compliance, ensuring an inclusive experience for all fans.

## Sustainability Considerations
- **Energy Optimization**: The `SustainabilityAgent` actively correlates crowd density with HVAC and lighting systems to recommend resource throttling in low-occupancy sectors.
- **Waste Management**: Predictive models alert janitorial staff before waste bins reach capacity, streamlining physical operations and reducing overflow.

## Testing
- **Unit Tests**: Domain models and orchestrator logic are isolated for unit testing.
- **Mock LLM Providers**: The `ILLMProvider` interface allows dependency injection of mock LLMs to test orchestration logic without incurring API costs.

## Assumptions
- The stadium is equipped with modern IoT infrastructure (smart turnstiles, CCTV crowd estimation, smart HVAC).
- Real-time transit feeds (city buses, trains) provide accessible APIs for data ingestion.

## Future Enhancements
- **WebSockets Integration**: Stream live events directly from the backend to the React Digital Twin in real-time.
- **Multi-modal Input**: Allow the AI to ingest audio transcripts from volunteer radios or images directly from security cameras.
- **Mobile App for Volunteers**: Send the synthesized action plans directly to the mobile devices of on-the-ground staff.

## License
MIT License. See `LICENSE` for details.
