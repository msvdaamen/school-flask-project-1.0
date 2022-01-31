import os

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app import db, app


class Image(db.Model):
    __tablename__ = 'images'

    id = Column(Integer, primary_key=True, autoincrement=True)
    filename = Column(String(255), nullable=False)
    movie_cover = relationship("Movie", back_populates="cover", foreign_keys='Movie.cover_id', uselist=False)
    movie_banner = relationship("Movie", back_populates="banner", foreign_keys='Movie.banner_id', uselist=False)

    def __init__(self, filename):
        self.filename = filename


    def toJson(self):
        return {
            'id': self.id,
            'filename': self.filename
        }

    def delete(delete_id):
        image = Image.query.filter(Image.id == delete_id).first()
        if image:
            Image.query.filter(Image.id == delete_id).delete()
            os.remove(os.path.join(app.config['UPLOAD_FOLDER'], image.filename))
            db.session.commit()
