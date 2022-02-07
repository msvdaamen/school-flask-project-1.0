from sqlalchemy import Column, Integer, String, UniqueConstraint
from sqlalchemy.orm import relationship

from app import db


class Actor(db.Model):
    __tablename__ = 'actors'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    __table_args__ = (UniqueConstraint('first_name', 'last_name', name='actors_first_last_name_uc'),)
    movieRole = relationship("MovieRole", back_populates="actor", uselist=False)


    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
