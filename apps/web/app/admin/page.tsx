const metrics = [
  { label: 'New signups', value: '128' },
  { label: 'Paid users', value: '19' },
  { label: 'MRR', value: '$890' },
  { label: 'Open support items', value: '6' },
];

export default function AdminPage() {
  return (
    <div className="mx-auto max-w-6xl px-6 py-10">
      <div className="mb-8">
        <p className="text-sm uppercase tracking-[0.2em] text-sky-400">Admin</p>
        <h1 className="mt-2 text-3xl font-bold">Business control panel</h1>
      </div>

      <div className="grid gap-4 md:grid-cols-4">
        {metrics.map((metric) => (
          <div key={metric.label} className="rounded-3xl border border-slate-800 bg-slate-900 p-5">
            <p className="text-sm text-slate-400">{metric.label}</p>
            <p className="mt-3 text-2xl font-semibold">{metric.value}</p>
          </div>
        ))}
      </div>
    </div>
  );
}
