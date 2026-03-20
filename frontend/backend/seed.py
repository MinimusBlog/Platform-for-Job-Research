"""Seed script to create initial data in the database."""

from app.core.database import Base, engine, SessionLocal
from app.models.user import User
from app.core.security import get_password_hash


def run() -> None:
    """Create database tables and a default admin user."""
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    admin_email = "admin@example.com"
    existing = db.query(User).filter(User.email == admin_email).first()
    if not existing:
        admin = User(
            email=admin_email,
            full_name="Administrator",
            hashed_password=get_password_hash("admin123"),
            role="admin",
        )
        db.add(admin)
        db.commit()
        print("Created admin user: admin@example.com / admin123")
    else:
        print("Admin user already exists")

    db.close()


if __name__ == "__main__":
    run()
