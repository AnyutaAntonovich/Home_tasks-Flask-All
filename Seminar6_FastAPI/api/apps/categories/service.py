from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from apps.base_repo.base_class import BaseService
from .models import Category
from config.settings import get_session

class CategoriesService(BaseService[Category]):
    def __init__(self, db_session:Session):
        super(CategoriesService, self).__init__(Category, db_session)



def get_categories_service(db_session:AsyncSession = Depends(get_session)) -> CategoriesService:
    return CategoriesService(db_session)