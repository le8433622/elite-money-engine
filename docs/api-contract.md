# API Contract

## Base path
`/`

## Authentication
### POST /auth/register
Create a user account.

Request fields:
- full_name
- email
- password

### POST /auth/login
Authenticate user and return bearer token.

Request fields:
- email
- password

Response fields:
- access_token
- token_type

### GET /users/me
Return authenticated user profile.

## Transactions
### POST /transactions
Create a new transaction.

Fields:
- type: income or expense
- category
- amount
- note

### GET /transactions
List transactions for authenticated user.

## Dashboard
### GET /dashboard/overview
Return summary fields:
- total_income
- total_expense
- balance
- transaction_count

### GET /dashboard/advice
Return AI-style advice payload:
- headline
- insights

## Automation
### POST /automations/rules
Create automation rule.

Fields:
- name
- rule_type
- threshold_amount
- category optional

### GET /automations/rules
List all automation rules for authenticated user.

### POST /automations/rules/{rule_id}/disable
Disable an automation rule.

### GET /automations/check
Evaluate enabled rules against current transaction data.

Response fields:
- alert_count
- alerts

## Planned next endpoints
- wallets
- budgets
- goals
- notifications
- billing
- admin analytics
