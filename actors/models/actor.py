from sqlalchemy import Column, Integer, String, UniqueConstraint
from app import db


class Actor(db.Model):
    __tablename__ = 'actors'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    __table_args__ = (UniqueConstraint('first_name', 'last_name', name='actors_first_last_name_uc'),)