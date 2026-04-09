export default function TransactionsPage() {
  return (
    <div className="mx-auto max-w-6xl px-6 py-10">
      <div className="mb-8">
        <p className="text-sm uppercase tracking-[0.2em] text-sky-400">Transactions</p>
        <h1 className="mt-2 text-3xl font-bold">Transaction history</h1>
      </div>

      <div className="rounded-3xl border border-slate-800 bg-slate-900 p-6">
        <div className="space-y-4 text-slate-300">
          <div className="rounded-2xl bg-slate-950/80 p-4">Income — salary — 4,000 USD</div>
          <div className="rounded-2xl bg-slate-950/80 p-4">Expense — rent — 1,100 USD</div>
          <div className="rounded-2xl bg-slate-950/80 p-4">Expense — food — 280 USD</div>
          <div className="rounded-2xl bg-slate-950/80 p-4">Expense — shopping — 620 USD</div>
        </div>
      </div>
    </div>
  );
}
