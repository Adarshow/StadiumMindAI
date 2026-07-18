import { useState } from 'react'
import { DigitalTwin } from './components/DigitalTwin'
import { OperationalCards } from './components/OperationalCards'
import { AIReasoningTimeline } from './components/AIReasoningTimeline'
import { DecisionPanel } from './components/DecisionPanel'
import { IncidentCenter } from './components/IncidentCenter'

function App() {
  const [operatorLanguage, setOperatorLanguage] = useState('English')

  return (
    <div className="min-h-screen p-6 flex flex-col gap-6">
      
      {/* Header */}
      <header className="flex justify-between items-center mb-2">
        <div>
          <h1 className="text-2xl font-black tracking-tight text-white flex items-center gap-2">
            <div className="w-4 h-4 bg-stadium-accent rounded-sm rotate-45"></div>
            StadiumMind <span className="text-stadium-accent">AI</span>
          </h1>
          <p className="text-sm text-stadium-muted mt-1">Global Operations Command Center</p>
        </div>
        
        <div className="flex items-center gap-6">
          {/* Multilingual Selector */}
          <div className="flex items-center gap-2">
            <span className="text-xs text-stadium-muted uppercase font-bold tracking-wider">Locale:</span>
            <select 
              value={operatorLanguage}
              onChange={(e) => setOperatorLanguage(e.target.value)}
              className="bg-stadium-panel border border-gray-600 text-white text-sm rounded-md py-1 px-2 focus:ring-stadium-accent focus:border-stadium-accent outline-none"
              aria-label="Select Operator Language"
            >
              <option value="English">English</option>
              <option value="Spanish">Español</option>
              <option value="French">Français</option>
              <option value="Arabic">العربية</option>
            </select>
          </div>

          <div className="text-right">
            <div className="text-sm font-mono text-white">14:04:32 PM</div>
            <div className="text-xs text-stadium-muted">Event Day 12 - Group Stage</div>
          </div>
          <div className="h-10 w-10 rounded-full bg-stadium-panel border-2 border-gray-600 flex items-center justify-center font-bold text-gray-300">
            OP
          </div>
        </div>
      </header>

      {/* Main Grid Dashboard */}
      <main className="grid grid-cols-1 lg:grid-cols-4 gap-6 flex-1">
        
        {/* Top Row: Digital Twin and Timeline */}
        <DigitalTwin />
        <IncidentCenter />
        <AIReasoningTimeline />

        {/* Middle Row: Operational KPI Cards */}
        <OperationalCards />

        {/* Bottom Row: AI Decision Engine */}
        <DecisionPanel />
        
        <div className="panel col-span-1 lg:col-span-2 flex items-center justify-center p-6 text-center text-stadium-muted">
          <p className="text-sm max-w-sm">
            <strong className="text-gray-300 block mb-2">Proactive Mode Active</strong>
            StadiumMind AI is continuously monitoring 1,240 camera feeds, 45 transport schedules, and IoT sensors to predict and resolve operational bottlenecks.
          </p>
        </div>

      </main>
    </div>
  )
}

export default App
