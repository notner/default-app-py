from defaultapp.core.model.base import PsqlBase

from sqlalchemy import Integer
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped


class Log(PsqlBase):
    __tablename__: str = 'log'

    id = mapped_column(Integer, primary_key=True)
    data: Mapped[str]
