from sqlalchemy import Column, Integer, String, UniqueConstraint, ForeignKey, Date
from sqlalchemy.orm import relationship

from app import db


class Movie(db.Model):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True, autoincrement=True)
    director_id = Column(Integer, ForeignKey("directors.id", ondelete="CASCADE"), nullable=False)
    title = Column(String(255))
    date = Column(Date, nullable=False)
    cover_id = Column(Integer, ForeignKey('images.id', ondelete="RESTRICT"), nullable=False)
    cover = relationship("Image", back_populates="movie_cover", foreign_keys='Movie.cover_id', uselist=False)
    banner_id = Column(Integer, ForeignKey('images.id', ondelete="RESTRICT"), nullable=False)
    banner = relationship("Image", back_populates="movie_banner", foreign_keys='Movie.banner_id', uselist=False)

    def toJson(self):
        return {
            'id': self.id,
            'director_id': self.director_id,
            'title': self.title,
            'data': self.date
        }
