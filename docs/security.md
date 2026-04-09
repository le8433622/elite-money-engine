# Security

## Core principles
- never expose secrets in the repository
- keep authentication simple and correct first
- protect user data with least-privilege access
- log important security-sensitive actions

## Current baseline
- JWT authentication
- hashed passwords
- protected user endpoints

## Recommended next security steps
- rotate secret keys in production
- use environment variables only for secrets
- add refresh token strategy
- add email verification
- add password reset flow
- add rate limiting on auth endpoints
- add audit logging for admin-sensitive actions
- add dependency checks in CI

## Deployment guidance
- separate staging and production secrets
- restrict database access
- use HTTPS everywhere
- avoid storing secrets in client-side code

## Internal policy guidance
- do not share personal access tokens in chat
- do not commit credentials to GitHub
- use restricted-scope credentials for external systems
