import decimal
from typing import Optional, List

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from config.settings import Base
from apps.brands.models import Brands
from apps.categories.models import Categories

class Products(Base):
    __tablename__='products'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    price: Mapped[float]
    article: Mapped[str]
    image: Mapped[str]
    body: Mapped[str]
    category_id: Mapped[str] = mapped_column(ForeignKey('categories.id'))
    brand_id: Mapped[str] = mapped_column(ForeignKey('brands.id'))

    category:Mapped['Categories'] = relationship(Categories, lazy="joined")
    brand:Mapped['Brands'] = relationship(Brands, lazy="joined")

    def __str__(self) -> str:
        return self.name