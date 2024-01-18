from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Owner(db.Model, SerializerMixin):
    __tablename__ = 'owners'

    serialize_rules = ('-pets.owner',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)

    pets = db.relationship('Pet', backref='owner')

    def __repr__(self):
        return f'<Pet Owner {self.name}>'

class Pet(db.Model, SerializerMixin):
    __tablename__ = 'pets'

    serialize_rules = ('-owners.pet',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    species = db.Column(db.String)

    owner_id = db.Column(db.Integer, db.ForeignKey('owners.id'))

    def __repr__(self):
        return f'<Pet {self.name}, {self.species}>'