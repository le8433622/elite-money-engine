export default function LoginPage() {
  return (
    <div className="mx-auto flex min-h-[80vh] max-w-6xl items-center px-6 py-10">
      <div className="mx-auto w-full max-w-md rounded-3xl border border-slate-800 bg-slate-900 p-8">
        <p className="text-sm uppercase tracking-[0.2em] text-sky-400">Authentication</p>
        <h1 className="mt-2 text-3xl font-bold">Sign in</h1>
        <p className="mt-3 text-slate-300">Access your dashboard, budgets, and automation alerts.</p>

        <div className="mt-8 space-y-4">
          <div>
            <label className="mb-2 block text-sm text-slate-300">Email</label>
            <input className="w-full rounded-2xl border border-slate-700 bg-slate-950 px-4 py-3 text-slate-100 outline-none" placeholder="you@example.com" />
          </div>
          <div>
            <label className="mb-2 block text-sm text-slate-300">Password</label>
            <input type="password" className="w-full rounded-2xl border border-slate-700 bg-slate-950 px-4 py-3 text-slate-100 outline-none" placeholder="••••••••" />
          </div>
          <button className="w-full rounded-2xl bg-sky-500 px-4 py-3 font-medium text-slate-950">Sign in</button>
        </div>
      </div>
    </div>
  );
}
