import React from 'react';

export const DigitalTwin = React.memo(function DigitalTwin() {
  return (
      <div className="panel-header flex justify-between items-center">
        <span>Stadium Digital Twin</span>
        <div className="flex gap-2 text-xs">
          <span className="flex items-center gap-1"><div className="w-2 h-2 rounded-full bg-stadium-danger"></div> High Density</span>
          <span className="flex items-center gap-1"><div className="w-2 h-2 rounded-full bg-stadium-success"></div> Normal</span>
        </div>
      </div>
      <div className="panel-body h-full w-full flex items-center justify-center relative">
        {/* Placeholder for SVG/Canvas of a stadium */}
        <div className="absolute inset-0 bg-stadium-dark/50" style={{
          backgroundImage: 'radial-gradient(circle at center, #1e293b 0%, #0f172a 100%)',
          backgroundSize: '100% 100%'
        }}></div>
        
        {/* Simulated Stadium Shape */}
        <div className="relative w-64 h-96 border-4 border-gray-600 rounded-full flex items-center justify-center">
          <div className="w-32 h-64 border-2 border-gray-500 rounded-full"></div>
          {/* Heatmap Nodes */}
          <div className="absolute top-10 left-10 w-8 h-8 bg-stadium-danger/70 rounded-full blur-md animate-pulse"></div>
          <div className="absolute bottom-20 right-12 w-12 h-12 bg-stadium-warning/60 rounded-full blur-md"></div>
          
          {/* Section labels */}
          <span className="absolute top-4 left-1/2 -translate-x-1/2 text-xs text-stadium-muted">North Gate</span>
          <span className="absolute bottom-4 left-1/2 -translate-x-1/2 text-xs text-stadium-muted">South Gate</span>
          <span className="absolute left-[-20px] top-1/2 -translate-y-1/2 text-xs text-stadium-muted -rotate-90">West Concourse</span>
          <span className="absolute right-[-20px] top-1/2 -translate-y-1/2 text-xs text-stadium-muted rotate-90">East Concourse</span>
        </div>
      </div>
    </div>
  )
});
