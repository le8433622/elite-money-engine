export default function PricingPage() {
  return (
    <div className="mx-auto max-w-6xl px-6 py-10">
      <div className="mb-8">
        <p className="text-sm uppercase tracking-[0.2em] text-sky-400">Pricing</p>
        <h1 className="mt-2 text-3xl font-bold">Simple plans for launch</h1>
      </div>

      <div className="grid gap-6 md:grid-cols-3">
        <div className="rounded-3xl border border-slate-800 bg-slate-900 p-6">
          <h2 className="text-xl font-semibold">Free</h2>
          <p className="mt-3 text-3xl font-bold">0đ</p>
          <p className="mt-4 text-slate-300">Basic dashboard, limited transactions, limited automation.</p>
        </div>

        <div className="rounded-3xl border border-sky-500 bg-slate-900 p-6">
          <h2 className="text-xl font-semibold">Pro</h2>
          <p className="mt-3 text-3xl font-bold">199.000đ</p>
          <p className="mt-4 text-slate-300">Unlimited tracking, budgets, goals, richer automation and insights.</p>
        </div>

        <div className="rounded-3xl border border-slate-800 bg-slate-900 p-6">
          <h2 className="text-xl font-semibold">Business</h2>
          <p className="mt-3 text-3xl font-bold">Custom</p>
          <p className="mt-4 text-slate-300">Team usage, admin visibility, support and future multi-user workflows.</p>
        </div>
      </div>
    </div>
  );
}
