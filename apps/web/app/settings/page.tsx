export default function SettingsPage() {
  return (
    <div className="mx-auto max-w-5xl px-6 py-10">
      <div className="mb-8">
        <p className="text-sm uppercase tracking-[0.2em] text-sky-400">Settings</p>
        <h1 className="mt-2 text-3xl font-bold">Account and product settings</h1>
      </div>

      <div className="grid gap-6 md:grid-cols-2">
        <div className="rounded-3xl border border-slate-800 bg-slate-900 p-6">
          <h2 className="text-xl font-semibold">Profile</h2>
          <p className="mt-3 text-slate-300">Manage your account details, preferred currency, and profile settings.</p>
        </div>
        <div className="rounded-3xl border border-slate-800 bg-slate-900 p-6">
          <h2 className="text-xl font-semibold">Billing</h2>
          <p className="mt-3 text-slate-300">Review plan status, invoices, and future subscription controls.</p>
        </div>
        <div className="rounded-3xl border border-slate-800 bg-slate-900 p-6">
          <h2 className="text-xl font-semibold">Notifications</h2>
          <p className="mt-3 text-slate-300">Configure product alerts, finance warnings, and email delivery preferences.</p>
        </div>
        <div className="rounded-3xl border border-slate-800 bg-slate-900 p-6">
          <h2 className="text-xl font-semibold">Security</h2>
          <p className="mt-3 text-slate-300">Password, device, and future verification settings will live here.</p>
        </div>
      </div>
    </div>
  );
}
