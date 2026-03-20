"""Email notification and verification helpers."""


def send_verification_email(to_email: str, code: str) -> None:
    """Send an email containing a verification code or link."""
    # TODO: integrate with an email delivery provider.
    print(f"[email_service] send_verification_email to={to_email} code={code}")
