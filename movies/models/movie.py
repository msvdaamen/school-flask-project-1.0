from sqlalchemy import Column, Integer, String, UniqueConstraint, ForeignKey, Date, Text
from sqlalchemy.orm import relationship

from app import db


class Movie(db.Model):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True, autoincrement=True)
    director_id = Column(Integer, ForeignKey("directors.id", ondelete="CASCADE"), nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(Text(), nullable=False)
    date = Column(Date, nullable=False)
    cover_id = Column(Integer, ForeignKey('images.id', ondelete="RESTRICT"), nullable=False)
    cover = relationship("Image", back_populates="movie_cover", foreign_keys='Movie.cover_id', uselist=False)
    banner_id = Column(Integer, ForeignKey('images.id', ondelete="RESTRICT"), nullable=False)
    banner = relationship("Image", back_populates="movie_banner", foreign_keys='Movie.banner_id', uselist=False)

    def __init__(self, cover_id, banner_id, director_id, title, description, date):
        self.cover_id = cover_id
        self.banner_id = banner_id
        self.director_id = director_id
        self.title = title
        self.description = description
        self.date = date



    def toJson(self):
        json = {
            'id': self.id,
            'director_id': self.director_id,
            'title': self.title,
            'description': self.description,
            'date': self.date,
            'cover': None,
            'banner': None
        }
        if self.cover:
            json['cover'] = self.cover.toJson()
        if self.banner:
            json['banner'] = self.banner.toJson()
        return json
