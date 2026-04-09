export default function BudgetsPage() {
  return (
    <div className="mx-auto max-w-6xl px-6 py-10">
      <div className="mb-8">
        <p className="text-sm uppercase tracking-[0.2em] text-sky-400">Budgets</p>
        <h1 className="mt-2 text-3xl font-bold">Monthly budget planning</h1>
      </div>

      <div className="grid gap-6 md:grid-cols-3">
        <div className="rounded-3xl border border-slate-800 bg-slate-900 p-6">
          <h2 className="text-xl font-semibold">Food</h2>
          <p className="mt-3 text-slate-300">Limit: 400 USD</p>
          <p className="mt-2 text-slate-400">Used: 280 USD</p>
        </div>
        <div className="rounded-3xl border border-slate-800 bg-slate-900 p-6">
          <h2 className="text-xl font-semibold">Shopping</h2>
          <p className="mt-3 text-slate-300">Limit: 500 USD</p>
          <p className="mt-2 text-slate-400">Used: 620 USD</p>
        </div>
        <div className="rounded-3xl border border-slate-800 bg-slate-900 p-6">
          <h2 className="text-xl font-semibold">Rent</h2>
          <p className="mt-3 text-slate-300">Limit: 1,100 USD</p>
          <p className="mt-2 text-slate-400">Used: 1,100 USD</p>
        </div>
      </div>
    </div>
  );
}
