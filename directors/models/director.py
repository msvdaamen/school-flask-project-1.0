from sqlalchemy import UniqueConstraint, Column, Integer, String

from app import db

class Director(db.Model):
    __tablename__ = 'directors'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    __table_args__ = (UniqueConstraint('first_name', 'last_name', name='directors_first_last_name_uc'),)


    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name