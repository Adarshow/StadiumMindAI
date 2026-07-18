import React from 'react';

export const DecisionPanel = React.memo(function DecisionPanel({ plan, onGeneratePlan, loading }: { plan: any, onGeneratePlan: () => void, loading: boolean }) {
  const confidencePercent = plan ? Math.round(plan.overall_confidence * 100) : 0;
  const topAction = plan?.prioritized_actions?.[0]?.action;

  return (
    <section className="panel col-span-1 lg:col-span-2" aria-labelledby="decision-panel-title">
      <header id="decision-panel-title" className="panel-header bg-stadium-accent/10 border-b-stadium-accent/30 text-stadium-accent">
        Master Action Plan
      </header>
      <div className="panel-body">
        
        {loading ? (
          <div className="flex flex-col items-center justify-center py-8">
            <div className="w-8 h-8 border-4 border-stadium-accent border-t-transparent rounded-full animate-spin mb-4"></div>
            <p className="text-stadium-muted">StadiumMind AI is synthesizing data...</p>
          </div>
        ) : plan ? (
          <>
            <div className="flex justify-between items-start mb-4">
              <div>
                <h3 className="text-lg font-bold text-white">{topAction?.description || "No critical actions required"}</h3>
                <p className="text-sm text-gray-400 mt-1">Priority: {topAction?.priority || "Normal"} | Target: {topAction?.target_zone || "N/A"}</p>
              </div>
              <div className="flex flex-col items-end">
                <span className="text-xs text-stadium-muted mb-1">Confidence Score</span>
                <span className="text-2xl font-black text-stadium-success" aria-label={`${confidencePercent}% Confidence`}>{confidencePercent}%</span>
              </div>
            </div>

            <article className="bg-black/30 rounded-lg p-4 mb-4 border border-gray-700">
              <h4 className="text-xs font-semibold text-stadium-muted uppercase mb-2">Explainability Panel</h4>
              <p className="text-sm text-gray-300 leading-relaxed">
                {plan.synthesis_reasoning}
              </p>
            </article>

            <div className="flex gap-3">
              <button onClick={onGeneratePlan} type="button" aria-label="Execute Action Plan" className="flex-1 bg-stadium-accent hover:bg-blue-500 text-white font-medium py-2 px-4 rounded-lg transition-colors focus:ring-2 focus:ring-offset-2 focus:ring-stadium-accent focus:outline-none">
                Execute New Plan
              </button>
            </div>
          </>
        ) : (
          <div className="flex flex-col items-center justify-center py-8">
            <p className="text-stadium-muted mb-4">No active plan generated yet.</p>
            <button onClick={onGeneratePlan} type="button" className="bg-stadium-accent hover:bg-blue-500 text-white font-medium py-2 px-6 rounded-lg transition-colors">
              Analyze Current Context
            </button>
          </div>
        )}

      </div>
    </section>
  )
});
