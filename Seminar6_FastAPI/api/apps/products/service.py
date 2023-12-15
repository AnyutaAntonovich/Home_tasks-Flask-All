import os
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from apps.base_repo.base_class import BaseService
from .models import Products
from config.settings import get_session
from utils.save_image import image_add_origin


class ProductsService(BaseService[Products]):
    def __init__(self, db_session:Session):
        super(ProductsService, self).__init__(Products, db_session)

    async def create(self, product):
        path_folder = 'static/images/product'
        if not os.path.exists(path_folder):
            os.mkdir(path_folder)

        path_image = image_add_origin(product.image, path_folder)

        async with self.db_session as session:
            new_product = self.table(name = product.name,
                                    image = path_image,
                                    article = product.article,
                                    price = product.price,
                                    body = product.body,
                                    category_id = product.category_id,
                                    brand_id = product.brand_id)
            session.add(new_product)
            await session.commit()

        return new_product


def get_product_service(db_session:AsyncSession = Depends(get_session)) -> ProductsService:
    return ProductsService(db_session)