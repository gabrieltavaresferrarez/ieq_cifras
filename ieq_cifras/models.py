from .Extensions.database import database
from flask_login import UserMixin


class Band(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(50), nullable=False)
    id_manager = database.Column(database.Integer, database.ForeignKey('user.id'), nullable=False)
    is_del = database.Column(database.Boolean, nullable=False, default=False)

    cifras = database.relationship('Cifra', backref='cifras', lazy=True)

    @property
    def users(self):
        list_bandMembers =  BandMember.query.filter_by(id_user = self.id, is_del=False).all()
        list_userIds = [bandMember.id_user for bandMember in list_bandMembers]
        return database.session.query(User).filter(User.id.in_(list_userIds)).all()

class User(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String(50), nullable=False)
    email = database.Column(database.String(50), nullable=False)
    password = database.Column(database.String(100), nullable=False)
    is_del = database.Column(database.Boolean, nullable=False, default=False)

    def __repr__(self) -> str:
        return f'User {self.username} (id : {self.id})'
    
    @property
    def bands(self):
        list_bandMembers =  BandMember.query.filter_by(id_user = self.id, is_del=False).all()
        list_bandIds = [bandMember.id_band for bandMember in list_bandMembers]
        return database.session.query(Band).filter(Band.id.in_(list_bandIds))


class Cifra(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    id_band = database.Column(database.Integer, database.ForeignKey('band.id'), nullable=False)
    name = database.Column(database.String(50), nullable=False, default='')
    author = database.Column(database.String(50), nullable=False, default='')
    version = database.Column(database.String(50), nullable=False, default='Padrão')
    tom = database.Column(database.Integer, nullable=False)
    text = database.Column(database.Text, nullable=False)
    estruct = database.Column(database.Text, nullable=False)
    is_del = database.Column(database.Boolean, nullable=False, default=False)

class BandMember(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    id_band = database.Column(database.Integer, database.ForeignKey('band.id'), nullable=False)
    id_user = database.Column(database.Integer, database.ForeignKey('user.id'), nullable=False)
    is_del = database.Column(database.Boolean, nullable=False, default=False)


class RegAuditCifra(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    id_cifra = database.Column(database.Integer, database.ForeignKey('cifra.id'), nullable=False)
    version = database.Column(database.String(50))
    id_user = database.Column(database.Integer, database.ForeignKey('user.id'), nullable=False)
    comment = database.Column(database.Text, nullable=False)
    is_del = database.Column(database.Boolean, nullable=False, default=False)

