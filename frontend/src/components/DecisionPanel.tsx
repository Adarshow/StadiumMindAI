export function DecisionPanel() {
  return (
    <section className="panel col-span-1 lg:col-span-2" aria-labelledby="decision-panel-title">
      <header id="decision-panel-title" className="panel-header bg-stadium-accent/10 border-b-stadium-accent/30 text-stadium-accent">
        Master Action Plan
      </header>
      <div className="panel-body">
        
        <div className="flex justify-between items-start mb-4">
          <div>
            <h3 className="text-lg font-bold text-white">Redirect Flow to East Concourse</h3>
            <p className="text-sm text-gray-400 mt-1">Preemptive measure to prevent North Gate bottleneck.</p>
          </div>
          <div className="flex flex-col items-end">
            <span className="text-xs text-stadium-muted mb-1">Confidence Score</span>
            <span className="text-2xl font-black text-stadium-success" aria-label="94% Confidence">94%</span>
          </div>
        </div>

        <article className="bg-black/30 rounded-lg p-4 mb-4 border border-gray-700">
          <h4 className="text-xs font-semibold text-stadium-muted uppercase mb-2">Explainability Panel</h4>
          <p className="text-sm text-gray-300 leading-relaxed">
            Based on historical data and current transit feeds, the arrival of 3 shuttles will increase North Gate density to unsafe levels (95%+) within 10 minutes. The East Concourse currently operates at 40% capacity. Redirecting traffic will balance the load and maintain optimal fan experience and safety metrics.
          </p>
        </article>

        <div className="flex gap-3">
          <button type="button" aria-label="Execute Action Plan" className="flex-1 bg-stadium-accent hover:bg-blue-500 text-white font-medium py-2 px-4 rounded-lg transition-colors focus:ring-2 focus:ring-offset-2 focus:ring-stadium-accent focus:outline-none">
            Execute Plan
          </button>
          <button type="button" aria-label="Modify Action Plan" className="flex-1 bg-gray-700 hover:bg-gray-600 text-white font-medium py-2 px-4 rounded-lg transition-colors focus:ring-2 focus:ring-offset-2 focus:ring-gray-500 focus:outline-none">
            Modify
          </button>
        </div>

      </div>
    </section>
  )
}
