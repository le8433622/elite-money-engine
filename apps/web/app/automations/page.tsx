export default function AutomationsPage() {
  return (
    <div className="mx-auto max-w-6xl px-6 py-10">
      <div className="mb-8">
        <p className="text-sm uppercase tracking-[0.2em] text-sky-400">Automations</p>
        <h1 className="mt-2 text-3xl font-bold">Automation rules and alerts</h1>
      </div>

      <div className="grid gap-6 md:grid-cols-2">
        <div className="rounded-3xl border border-slate-800 bg-slate-900 p-6">
          <h2 className="text-xl font-semibold">Rule types</h2>
          <div className="mt-4 space-y-3 text-slate-300">
            <div className="rounded-2xl bg-slate-950/80 p-4">Low balance guard</div>
            <div className="rounded-2xl bg-slate-950/80 p-4">Monthly expense cap</div>
            <div className="rounded-2xl bg-slate-950/80 p-4">Large expense detector</div>
          </div>
        </div>

        <div className="rounded-3xl border border-slate-800 bg-slate-900 p-6">
          <h2 className="text-xl font-semibold">Current alert summary</h2>
          <div className="mt-4 space-y-3 text-slate-300">
            <div className="rounded-2xl bg-slate-950/80 p-4">1 warning for low balance threshold</div>
            <div className="rounded-2xl bg-slate-950/80 p-4">1 warning for monthly shopping cap</div>
            <div className="rounded-2xl bg-slate-950/80 p-4">1 high-priority alert for recent large expense</div>
          </div>
        </div>
      </div>
    </div>
  );
}
