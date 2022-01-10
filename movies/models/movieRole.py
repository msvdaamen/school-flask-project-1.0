from app import db
from sqlalchemy import Column, Integer, String, UniqueConstraint, ForeignKey, Date

class MovieRole(db.Model):
    __tablename__ = 'movie_roles'

    id = Column(Integer, primary_key=True, autoincrement=True)
    movie_id = Column(Integer, ForeignKey("movies.id", ondelete="CASCADE"), nullable=False)
    actor_id = Column(Integer, ForeignKey("actors.id", ondelete="CASCADE"), nullable=False)
    name = Column(String(255), nullable=False)