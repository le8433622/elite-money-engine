const items = [
  'Product setup and onboarding',
  'Billing and subscription support',
  'Automation troubleshooting',
  'Bug reports and feature requests',
];

export default function SupportPage() {
  return (
    <div className="mx-auto max-w-5xl px-6 py-10">
      <div className="mb-8">
        <p className="text-sm uppercase tracking-[0.2em] text-sky-400">Support</p>
        <h1 className="mt-2 text-3xl font-bold">Customer support</h1>
      </div>

      <div className="grid gap-4">
        {items.map((item) => (
          <div key={item} className="rounded-3xl border border-slate-800 bg-slate-900 p-6 text-slate-200">
            {item}
          </div>
        ))}
      </div>
    </div>
  );
}
