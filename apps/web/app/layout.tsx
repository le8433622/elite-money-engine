export const metadata = {
  title: 'Elite Money Engine',
  description: 'Finance SaaS with automation and AI-assisted insights',
};

import './globals.css';
import Link from 'next/link';
import type { ReactNode } from 'react';

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en">
      <body>
        <div className="min-h-screen bg-slate-950 text-slate-100">
          <header className="border-b border-slate-800 bg-slate-900/80">
            <div className="mx-auto flex max-w-6xl items-center justify-between px-6 py-4">
              <Link href="/" className="text-lg font-semibold">
                Elite Money Engine
              </Link>
              <nav className="flex gap-6 text-sm text-slate-300">
                <Link href="/dashboard">Dashboard</Link>
                <Link href="/transactions">Transactions</Link>
                <Link href="/automations">Automations</Link>
                <Link href="/pricing">Pricing</Link>
              </nav>
            </div>
          </header>
          <main>{children}</main>
        </div>
      </body>
    </html>
  );
}
