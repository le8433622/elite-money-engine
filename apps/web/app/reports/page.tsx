const reports = [
  'Monthly cash flow summary',
  'Expense by category',
  'Budget variance review',
  'Automation alert history',
];

export default function ReportsPage() {
  return (
    <div className="mx-auto max-w-6xl px-6 py-10">
      <div className="mb-8">
        <p className="text-sm uppercase tracking-[0.2em] text-sky-400">Reports</p>
        <h1 className="mt-2 text-3xl font-bold">Financial reports</h1>
      </div>

      <div className="grid gap-4 md:grid-cols-2">
        {reports.map((report) => (
          <div key={report} className="rounded-3xl border border-slate-800 bg-slate-900 p-6 text-slate-200">
            {report}
          </div>
        ))}
      </div>
    </div>
  );
}
