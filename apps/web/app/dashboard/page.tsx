const cards = [
  { label: 'Total income', value: '$12,400' },
  { label: 'Total expense', value: '$7,180' },
  { label: 'Balance', value: '$5,220' },
  { label: 'Automation alerts', value: '3 active' },
];

const insights = [
  'Food and shopping are the highest expense groups this month.',
  'Savings rate is healthy but can improve if large discretionary spending is reduced.',
  'One automation rule detected a recent high-value expense that should be reviewed.',
];

export default function DashboardPage() {
  return (
    <div className="mx-auto flex max-w-6xl flex-col gap-8 px-6 py-10">
      <div>
        <p className="text-sm uppercase tracking-[0.2em] text-sky-400">Dashboard</p>
        <h1 className="mt-2 text-3xl font-bold">Financial overview</h1>
      </div>

      <section className="grid gap-4 md:grid-cols-4">
        {cards.map((card) => (
          <div key={card.label} className="rounded-3xl border border-slate-800 bg-slate-900 p-5">
            <p className="text-sm text-slate-400">{card.label}</p>
            <p className="mt-3 text-2xl font-semibold">{card.value}</p>
          </div>
        ))}
      </section>

      <section className="grid gap-6 md:grid-cols-[2fr_1fr]">
        <div className="rounded-3xl border border-slate-800 bg-slate-900 p-6">
          <h2 className="text-xl font-semibold">Cash flow summary</h2>
          <div className="mt-6 grid gap-3">
            <div className="rounded-2xl bg-slate-950/80 p-4 text-slate-300">Income performance is stable across the current cycle.</div>
            <div className="rounded-2xl bg-slate-950/80 p-4 text-slate-300">Expense concentration is trending toward lifestyle categories.</div>
            <div className="rounded-2xl bg-slate-950/80 p-4 text-slate-300">Budget controls should be added for shopping and food.</div>
          </div>
        </div>
        <div className="rounded-3xl border border-slate-800 bg-slate-900 p-6">
          <h2 className="text-xl font-semibold">AI-style insights</h2>
          <ul className="mt-4 space-y-3 text-sm text-slate-300">
            {insights.map((item) => (
              <li key={item} className="rounded-2xl bg-slate-950/80 p-4">
                {item}
              </li>
            ))}
          </ul>
        </div>
      </section>
    </div>
  );
}
