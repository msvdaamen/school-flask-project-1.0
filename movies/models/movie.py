from sqlalchemy import Column, Integer, String, UniqueConstraint, ForeignKey, Date
from app import db


class Movie(db.Model):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True, autoincrement=True)
    director_id = Column(Integer, ForeignKey("directors.id", ondelete="CASCADE"), nullable=False)
    title = Column(String(255))
    date = Column(Date, nullable=False)

    def toJson(self):
        return {
            'id': self.id,
            'director_id': self.director_id,
            'title': self.title,
            'data': self.date
        }
