from app.models import Photo
from app.db import db


get_photo_with_likes = db.session.query(Photo).filter(
    Photo.count_likes != 0).order_by(Photo.path_to_image).all()
