import React from 'react';

export const AIReasoningTimeline = React.memo(function AIReasoningTimeline() {
  return (
    <aside className="panel col-span-1 row-span-2" aria-labelledby="timeline-title">
      <header className="panel-header flex justify-between items-center">
        <span id="timeline-title">AI Reasoning Timeline</span>
        <span className="text-xs bg-stadium-accent/20 text-stadium-accent px-2 py-0.5 rounded" aria-hidden="true">Live</span>
      </header>
      <div className="panel-body overflow-y-auto max-h-[500px]" aria-live="polite" role="log">
        <ul className="relative pl-6 border-l border-gray-700 space-y-6" aria-label="Reasoning Event Log">
          
          <li className="relative">
            <div className="absolute -left-[31px] bg-stadium-dark border-2 border-stadium-warning w-4 h-4 rounded-full" aria-hidden="true"></div>
            <time dateTime="14:02" className="text-xs text-stadium-muted block mb-1">14:02 PM</time>
            <p className="text-sm font-semibold text-gray-200">Crowd Agent detected anomaly</p>
            <p className="text-xs text-gray-400 mt-1">Density at North Gate exceeded threshold (85%).</p>
          </li>

          <li className="relative">
            <div className="absolute -left-[31px] bg-stadium-dark border-2 border-stadium-accent w-4 h-4 rounded-full" aria-hidden="true"></div>
            <time dateTime="14:03" className="text-xs text-stadium-muted block mb-1">14:03 PM</time>
            <p className="text-sm font-semibold text-gray-200">Transport Agent correlation</p>
            <p className="text-xs text-gray-400 mt-1">Correlated with arrival of 3 shuttles from City Center simultaneously.</p>
          </li>

          <li className="relative">
            <div className="absolute -left-[31px] bg-stadium-dark border-2 border-stadium-success w-4 h-4 rounded-full" aria-hidden="true"></div>
            <time dateTime="14:04" className="text-xs text-stadium-muted block mb-1">14:04 PM</time>
            <p className="text-sm font-semibold text-gray-200">Master Orchestrator Synthesis</p>
            <p className="text-xs text-gray-400 mt-1">Synthesizing findings to generate preemptive crowd redistribution plan.</p>
          </li>

        </ul>
      </div>
    </aside>
  )
});
