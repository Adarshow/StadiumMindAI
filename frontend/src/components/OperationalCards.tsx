import React from 'react';

export const OperationalCards = React.memo(function OperationalCards() {
  return (
    <section className="col-span-1 lg:col-span-3 grid grid-cols-1 md:grid-cols-3 gap-4" aria-label="Operational Key Performance Indicators">
      {/* Transportation */}
      <article className="panel">
        <header className="panel-header">Transportation Status</header>
        <div className="panel-body">
          <div className="flex justify-between items-center mb-2">
            <span className="text-gray-300 font-medium">Shuttle Arrival</span>
            <span className="text-stadium-warning font-bold" aria-live="polite">Surge in 15m</span>
          </div>
          <div className="w-full bg-gray-700 h-2 rounded-full overflow-hidden" role="progressbar" aria-valuenow={85} aria-valuemin={0} aria-valuemax={100}>
            <div className="bg-stadium-warning h-full w-[85%]"></div>
          </div>
          <p className="text-xs text-stadium-muted mt-2">Parking Lot C at 92% capacity.</p>
        </div>
      </article>

      {/* Accessibility */}
      <article className="panel border-l-4 border-l-stadium-accent">
        <header className="panel-header">Accessibility Monitor</header>
        <div className="panel-body" aria-live="polite">
           <div className="flex justify-between items-center mb-2">
            <span className="text-gray-300 font-medium">Wheelchair Requests</span>
            <span className="text-stadium-success font-bold">Fulfilled</span>
          </div>
           <div className="flex justify-between items-center">
            <span className="text-gray-300 text-sm">Sensory Room A</span>
            <span className="text-stadium-success text-sm">Available</span>
          </div>
          <div className="flex justify-between items-center mt-1">
            <span className="text-gray-300 text-sm">Sensory Room B</span>
            <span className="text-stadium-danger text-sm">Occupied</span>
          </div>
        </div>
      </article>

      {/* Sustainability */}
      <article className="panel">
        <header className="panel-header">Sustainability Insights</header>
        <div className="panel-body">
          <div className="flex justify-between items-center mb-2">
            <span className="text-gray-300 font-medium">Energy Load</span>
            <span className="text-stadium-accent font-bold" aria-live="polite">Optimized</span>
          </div>
          <div className="w-full bg-gray-700 h-2 rounded-full overflow-hidden" role="progressbar" aria-valuenow={60} aria-valuemin={0} aria-valuemax={100}>
            <div className="bg-stadium-accent h-full w-[60%]"></div>
          </div>
          <p className="text-xs text-stadium-muted mt-2">Sector 4 HVAC reduced due to low occupancy.</p>
        </div>
      </article>
    </section>
  )
});
