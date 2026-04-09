# Deployment

## Early stage deployment
### Frontend
- deploy web app on Vercel
- configure environment variables for API base URL and product analytics

### Backend
- deploy FastAPI service on Render, Fly.io, or Railway
- use managed PostgreSQL
- use managed Redis when background jobs are introduced

## Required environment variables
### API
- APP_NAME
- SECRET_KEY
- ACCESS_TOKEN_EXPIRE_MINUTES
- DATABASE_URL

### Web
- NEXT_PUBLIC_API_BASE_URL
- NEXT_PUBLIC_APP_NAME

## Release environments
- local
- staging
- production

## Recommended steps
1. push code to GitHub
2. connect repo to deployment provider
3. configure environment variables
4. run database migrations
5. verify health endpoint
6. smoke test onboarding and dashboard flows

## Future deployment improvements
- add CI checks
- run tests before deploy
- add worker process for notifications and reports
- add error monitoring
- add uptime checks
