from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app import db


class Image(db.Model):
    __tablename__ = 'images'

    id = Column(Integer, primary_key=True, autoincrement=True)
    filename = Column(String(255), nullable=False)
    movie_cover = relationship("Movie", back_populates="cover", foreign_keys='Movie.cover_id', uselist=False)
    movie_banner = relationship("Movie", back_populates="banner", foreign_keys='Movie.banner_id', uselist=False)