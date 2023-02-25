from datetime import datetime
from app.db import db


class CultureOrganization(db.Model):

    # таблица хранения данных об организации культуры

    __tablename__ = 'culture_organizations'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    address = db.Column(db.String, nullable=False)
    phone_number = db.Column(db.String, nullable=True)
    web_site = db.Column(db.String, nullable=True)

    def __repr__(self):
        return 'Company {}, id - {}'.format(self.name, self.id)


class Photo(db.Model):

    # таблица хранения информации о фотографиях,
    # которые были сделаны в организациях культуры

    __tablename__ = 'photos'

    id = db.Column(db.Integer, primary_key=True)
    culture_organization_id = db.Column(
        db.Integer,
        db.ForeignKey('culture_organizations.id', ondelete='CASCADE'),
        nullable=False,)
    path_to_image = db.Column(
        db.String, index=True, unique=True, nullable=False)
    count_likes = db.Column(db.Integer, default=0)
    create_date = db.Column(
        db.DateTime, nullable=False, default=datetime.now())

    def __repr__(self):
        return 'Organization id - {}, id - {}'.format(
            self.culture_organization_id, self.id)
