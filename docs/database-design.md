# Database Design

## Current core tables
### users
- id
- full_name
- email
- password_hash
- created_at

### transactions
- id
- user_id
- type
- category
- amount
- note
- created_at

### automation_rules
- id
- user_id
- name
- rule_type
- category
- threshold_amount
- is_enabled
- created_at

## Recommended next tables
### wallets
Purpose: separate money sources and balances.

Suggested fields:
- id
- user_id
- name
- currency
- starting_balance
- current_balance optional derived
- created_at

### budgets
Purpose: define spending limits by cycle and category.

Suggested fields:
- id
- user_id
- name
- category optional
- limit_amount
- period_type monthly by default
- start_date
- end_date optional
- is_enabled

### goals
Purpose: track savings and finance targets.

Suggested fields:
- id
- user_id
- name
- target_amount
- current_amount
- deadline optional
- status

### notifications
Purpose: persist alerts sent to user.

Suggested fields:
- id
- user_id
- channel
- title
- body
- is_read
- created_at

### subscriptions
Purpose: billing state and plan tracking.

Suggested fields:
- id
- user_id
- provider
- external_subscription_id
- plan_code
- status
- current_period_start
- current_period_end

## Relationship overview
- one user has many transactions
- one user has many automation rules
- one user can have many wallets
- one user can have many budgets
- one user can have many goals
- one user can have many notifications
- one user can have one active subscription record

## Index guidance
Recommended indexes:
- users.email unique
- transactions.user_id
- transactions.created_at
- transactions.user_id + created_at
- automation_rules.user_id
- budgets.user_id
- goals.user_id
- notifications.user_id + created_at

## Migration priority
1. wallets
2. budgets
3. goals
4. notifications
5. subscriptions
