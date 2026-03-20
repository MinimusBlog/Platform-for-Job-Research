"""API router package."""

from fastapi import APIRouter

from . import (
    auth,
    opportunities,
    applications,
    users,
    employers,
    curator,
    tags,
)

router = APIRouter()

router.include_router(auth.router, prefix="/auth", tags=["auth"])
router.include_router(opportunities.router, prefix="/opportunities", tags=["opportunities"])
router.include_router(applications.router, prefix="/applications", tags=["applications"])
router.include_router(users.router, prefix="/users", tags=["users"])
router.include_router(employers.router, prefix="/employers", tags=["employers"])
router.include_router(curator.router, prefix="/curator", tags=["curator"])
router.include_router(tags.router, prefix="/tags", tags=["tags"])
