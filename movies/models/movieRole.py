from sqlalchemy.orm import relationship

from app import db
from sqlalchemy import Column, Integer, String, UniqueConstraint, ForeignKey, Date

class MovieRole(db.Model):
    __tablename__ = 'movie_roles'

    id = Column(Integer, primary_key=True, autoincrement=True)
    movie_id = Column(Integer, ForeignKey("movies.id", ondelete="CASCADE"), nullable=False)
    actor_id = Column(Integer, ForeignKey("actors.id", ondelete="CASCADE"), nullable=False)
    name = Column(String(255), nullable=False)
    movie = relationship("Movie", back_populates="movieRole", foreign_keys='MovieRole.movie_id', uselist=False)
    actor = relationship("Actor", back_populates="movieRole", foreign_keys='MovieRole.actor_id', uselist=False)


    def __init__(self, movie_id, actor_id, name):
        self.movie_id = movie_id
        self.actor_id = actor_id
        self.name = name

    def toJson(self):
        json = {
            'id': self.id,
            'movie_id': self.movie_id,
            'actor_id': self.actor_id,
            'name': self.name
        }
        return json