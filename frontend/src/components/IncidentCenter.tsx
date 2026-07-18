export function IncidentCenter() {
  return (
    <section className="panel col-span-1" aria-labelledby="incident-center-title">
      <header id="incident-center-title" className="panel-header">Active Incidents</header>
      <div className="panel-body p-0" aria-live="polite" role="status">
        <ul className="divide-y divide-gray-700/50" role="list" aria-label="List of active and resolved incidents">
          
          <li className="p-4 hover:bg-white/5 transition-colors cursor-pointer" tabIndex={0}>
            <div className="flex justify-between mb-1">
              <span className="text-sm font-semibold text-white">Medical Emergency</span>
              <span className="text-xs font-mono text-stadium-danger bg-stadium-danger/10 px-1.5 rounded" aria-label="Severity Critical">CRITICAL</span>
            </div>
            <p className="text-xs text-gray-400">Section 104, Row G. Medic team dispatched. ETA 2m.</p>
          </li>

          <li className="p-4 hover:bg-white/5 transition-colors cursor-pointer" tabIndex={0}>
            <div className="flex justify-between mb-1">
              <span className="text-sm font-semibold text-white">Spill on Concourse</span>
              <span className="text-xs font-mono text-stadium-warning bg-stadium-warning/10 px-1.5 rounded" aria-label="Severity Moderate">MODERATE</span>
            </div>
            <p className="text-xs text-gray-400">West Concourse near Gate B. Janitorial notified.</p>
          </li>

          <li className="p-4 hover:bg-white/5 transition-colors cursor-pointer opacity-60" tabIndex={0}>
            <div className="flex justify-between mb-1">
              <span className="text-sm font-semibold text-white line-through">Turnstile Malfunction</span>
              <span className="text-xs font-mono text-stadium-success bg-stadium-success/10 px-1.5 rounded" aria-label="Resolved">RESOLVED</span>
            </div>
            <p className="text-xs text-gray-400">Gate C. Maintenance repaired at 13:45 PM.</p>
          </li>

        </ul>
      </div>
    </section>
  )
}
