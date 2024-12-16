# SendingEmails

Django app implementing email-based account verification with two confirmation methods: a short verification code and a one-time activation link.

Accounts are created with `is_active=False`. The user is only activated after verifying their email, preventing access with unverified addresses.

---

## Verification flows

**Link-based** (UID + token in URL):
1. User registers → account created with `is_active=False`
2. Email sent with activation URL: `/activate_account/<uidb64>/<token>/`
3. User clicks link → `ActivateAccountView` validates token, sets `is_active=True`

Token generation uses `AccountActivationTokenGenerator`, a subclass of Django's `PasswordResetTokenGenerator` — so tokens are time-limited and single-use.

**Code-based**:
1. User submits registration form
2. Short code sent to email
3. User enters code at `/accounts/verify_email/`
4. Account activated on match

---

## Notable details

- `CreateUserForm(UserCreationForm)` validates email uniqueness before saving — the default Django user form doesn't enforce this.
- New accounts default to `is_active=False` inside `form.save()`, not in a view — the constraint holds regardless of how users are created.
- Custom `AccountActivationTokenGenerator` reuses Django's HMAC-based token mechanism, so tokens invalidate after the user logs in or the password changes.

---

## Stack

| Layer | Technology |
|---|---|
| Backend | Django 5.1 |
| DB | SQLite (dev) |
| Auth | Django built-in + custom token generator |
| Email | Django `send_mail` (SMTP) |

---

## Getting started

```bash
python manage.py migrate
python manage.py runserver
```

Configure email in `settings.py`:
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.example.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = '...'
EMAIL_HOST_PASSWORD = '...'
```

Routes: `POST /accounts/register/`, `GET /accounts/verify_email/`, `GET /activate_account/<uidb64>/<token>/`.

> **Status**: core verification flow is working. Email template styling is minimal — suitable as a reference implementation.
