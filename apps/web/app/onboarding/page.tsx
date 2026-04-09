const steps = [
  'Create your account and confirm basic profile details.',
  'Add your first income and expense records.',
  'Create monthly budgets for key categories.',
  'Enable automation rules for risk monitoring.',
  'Review dashboard insights and adjust spending behavior.',
];

export default function OnboardingPage() {
  return (
    <div className="mx-auto max-w-5xl px-6 py-10">
      <div className="mb-8">
        <p className="text-sm uppercase tracking-[0.2em] text-sky-400">Onboarding</p>
        <h1 className="mt-2 text-3xl font-bold">Get started in five steps</h1>
      </div>

      <div className="grid gap-4">
        {steps.map((step, index) => (
          <div key={step} className="rounded-3xl border border-slate-800 bg-slate-900 p-6">
            <div className="mb-3 inline-flex h-8 w-8 items-center justify-center rounded-full bg-sky-500 font-semibold text-slate-950">
              {index + 1}
            </div>
            <p className="text-slate-200">{step}</p>
          </div>
        ))}
      </div>
    </div>
  );
}
