from flask import Flask, make_response, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from models import db, Owner, Pet

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return '<h1>Welcome to my pet store!</h1>'
@app.route('/pets')
def pets():
    pets = []
    for pet in Pet.query.all():
        pet_dict = {
            "species": pet.species,
            "name": pet.name,
        }
        pets.append(pet_dict)
    response = make_response(jsonify(pets), 200)
    response.headers["Content_Type"] = "application/json"
    return response

@app.route('/owners')
def owners():
    owners = Owner.query.all()
    return owners.to_dict()

@app.route('/owner/<int:id>')
def owner_by_id(id):
    owner = Owner.query.get(id)
    return owner.to_dict()

@app.route('/owners/<int:id>')
def owners_id(id):
    oners = Owner.query.filter_by(id=id).first()
    return oners.to_dict()
    




if __name__ == '__main__':
    app.run(port=5555)