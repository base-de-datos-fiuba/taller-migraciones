from fastapi import APIRouter
from src.service.users import UserService

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/")
def get_users_with_age():
    """
    Retrieve users with their age calculated from birthdate.
    """
    users = []
    # users = UserService.get_users_with_age()
    return {"users": users}


@router.get("/users_age_sqlalchemy", summary="Get users with age using SQLAlchemy")
def get_users_with_age_sqlalchemy():
    """
    Retrieve users with their age calculated from birthdate using SQLAlchemy.
    """
    users = UserService.get_users_with_age_sqlalchemy()
    return {"users": users}
