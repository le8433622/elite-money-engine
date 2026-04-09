# Architecture

## Overview
Elite Money Engine should evolve as a fullstack SaaS with a separate frontend app and backend API.

## Frontend
- Next.js
- TypeScript
- Tailwind CSS
- Component-based dashboard UI
- API client layer for backend integration

## Backend
- FastAPI
- SQLAlchemy
- PostgreSQL
- Redis for caching and queued jobs
- Background workers for notifications and reports

## Core backend modules
- auth
- users
- wallets
- transactions
- budgets
- goals
- automation
- ai_insights
- notifications
- billing
- admin

## Infrastructure
### Early stage
- Vercel for web
- Render or Fly.io for API
- Managed Postgres
- Managed Redis
- Stripe for billing
- Resend or Postmark for email

### Growth stage
- Dockerized services
- Separate worker process
- Observability with logs and error tracking
- CI/CD for web and API

## Suggested repo direction
### Option A: monorepo
- apps/web
- apps/api
- docs
- scripts

### Option B: two repos
- elite-money-engine-web
- elite-money-engine-api

Monorepo is recommended once the product grows and shared types become valuable.
