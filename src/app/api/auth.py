"""Api urls and views for users"""
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from ..database import get_session
from ..models.auth import User, UserCreate, Token
from ..services.auth import AuthService, get_current_user


router = APIRouter()


@router.post('/sign-up', response_model=Token)
def sign_up(user_data: UserCreate, session: Session = Depends(get_session)):
    """Registration"""
    service = AuthService(session=session)
    return service.register_new_user(user_data)


@router.post('/sign-in', response_model=Token)
def sign_in(
    form_data: OAuth2PasswordRequestForm = Depends(),
    session: Session = Depends(get_session)
    ):
    """Autorization"""
    service = AuthService(session=session)
    return service.authenticate_user(
        form_data.username,
        form_data.password
    )


@router.get('/user', response_model=User)
def get_user(user: User = Depends(get_current_user)):
    """Getting one user"""
    return user
