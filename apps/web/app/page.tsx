import Link from 'next/link';

const features = [
  'Cash flow dashboard',
  'Budget and savings planning',
  'Automation rules and alerts',
  'AI-assisted financial insights',
];

export default function HomePage() {
  return (
    <div className="mx-auto flex max-w-6xl flex-col gap-16 px-6 py-16">
      <section className="grid gap-10 md:grid-cols-2 md:items-center">
        <div className="space-y-6">
          <p className="text-sm uppercase tracking-[0.2em] text-sky-400">Finance SaaS for real-world use</p>
          <h1 className="text-4xl font-bold leading-tight md:text-6xl">
            Track money, automate alerts, and turn data into better decisions.
          </h1>
          <p className="max-w-xl text-base text-slate-300 md:text-lg">
            Elite Money Engine helps individuals, freelancers, and small teams manage transactions,
            budgets, automation rules, and AI-style insights in one product.
          </p>
          <div className="flex flex-wrap gap-4">
            <Link href="/dashboard" className="rounded-xl bg-sky-500 px-5 py-3 font-medium text-slate-950">
              Open dashboard
            </Link>
            <Link href="/pricing" className="rounded-xl border border-slate-700 px-5 py-3 font-medium">
              View pricing
            </Link>
          </div>
        </div>
        <div className="rounded-3xl border border-slate-800 bg-slate-900 p-8 shadow-2xl shadow-slate-950/40">
          <div className="grid gap-4">
            {features.map((feature) => (
              <div key={feature} className="rounded-2xl border border-slate-800 bg-slate-950/70 p-4 text-slate-200">
                {feature}
              </div>
            ))}
          </div>
        </div>
      </section>

      <section className="grid gap-6 md:grid-cols-3">
        <div className="rounded-3xl border border-slate-800 bg-slate-900 p-6">
          <h2 className="text-xl font-semibold">Automation-first</h2>
          <p className="mt-3 text-slate-300">
            Create rules for low balance, monthly budget caps, and large expenses.
          </p>
        </div>
        <div className="rounded-3xl border border-slate-800 bg-slate-900 p-6">
          <h2 className="text-xl font-semibold">Built for subscription SaaS</h2>
          <p className="mt-3 text-slate-300">
            Product direction includes billing, onboarding, retention metrics, and admin visibility.
          </p>
        </div>
        <div className="rounded-3xl border border-slate-800 bg-slate-900 p-6">
          <h2 className="text-xl font-semibold">Ready to grow</h2>
          <p className="mt-3 text-slate-300">
            Start with web, then expand into advanced AI insights, reports, and team workflows.
          </p>
        </div>
      </section>
    </div>
  );
}
