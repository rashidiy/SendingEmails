# SendingEmails

Django app for email-based account verification. Supports two verification flows — a code sent to the user's email, or a one-time confirmation link.

## Stack

- **Backend**: Django
- **DB**: SQLite (dev) / PostgreSQL

## Features

- User registration with email verification
- Two verification methods:
  - Code-based — a short code is emailed, user enters it on the site
  - Link-based — a one-time URL is emailed, user clicks to verify
- Custom token generation (accounts/tokens.py)
- Auth views: sign-up, sign-in, email verification

## Project Structure

```
accounts/
  models.py       — user model
  views.py        — registration and verification views
  services.py     — email sending logic
  tokens.py       — token generation for email links
  forms.py        — registration/login forms
  urls.py

templates/
  auth/
    sign-up.html
    sign-in.html
    email_verification.html
```

## Getting Started

```bash
pip install -r requirements.txt
cp .env.example .env    # set EMAIL_HOST, EMAIL_PORT, etc.
python manage.py migrate
python manage.py runserver
```
