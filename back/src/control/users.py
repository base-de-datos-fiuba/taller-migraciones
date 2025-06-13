from fastapi import APIRouter
from src.service.users import UserService

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/users_age", summary="Get users with age")
def get_users_with_age():
    """
    Retrieve users with their age calculated from birthdate.
    """
    users = []
    # users = UserService.get_users_with_age()
    return {"users": users}

