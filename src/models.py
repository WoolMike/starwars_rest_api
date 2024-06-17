from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship


db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    # is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    favorites_characters = db.relationship('FavoritesCharacters', backref='user', lazy=True)
    favorites_planets = db.relationship('FavoritesPlanets', backref='user', lazy=True)
    favorites_vehicles = db.relationship('FavoritesVehicles', backref='user', lazy=True)

    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email
            # do not serialize the password, its a security breach
        }

class Character(db.Model):
    __tablename__ = 'character'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    height = db.Column(db.Integer)
    url = db.Column(db.String(80))
    description = db.Column(db.String(80))
    eye_color = db.Column(db.String(80))
    hair_color = db.Column(db.String(80))
    skin_color = db.Column(db.String(80))
    favorites_characters = db.relationship('FavoritesCharacters', backref='character', lazy=True)


    def __repr__(self):
        return '<Character %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "url": self.url,
            "description": self.description,
            "eye_color": self.eye_color,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color
            # do not serialize the password, its a security breach
        } 

class Planet(db.Model):
    __tablename__ = 'planet'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    climate = db.Column(db.String(80))
    diameter = db.Column(db.Integer)
    gravity = db.Column(db.Integer)
    orbital_period = db.Column(db.Integer)
    population = db.Column(db.Integer)
    rotational_period = db.Column(db.Integer)
    surface_water = db.Column(db.Integer)
    terrain = db.Column(db.String(80))
    favorites_planets = db.relationship('FavoritesPlanets', backref='planet', lazy=True)


    def __repr__(self):
        return '<Planet %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "climate": self.climate,
            "diameter": self.diameter,
            "gravity": self.gravity,
            "orbital_period": self.orbital_period,
            "population": self.population,
            "rotational_period": self.rotational_period,
            "surface_water": self.surface_water,
            "terrain": self.terrain
            # do not serialize the password, its a security breach
        }  

class Vehicle(db.Model):
    __tablename__ = 'vehicle'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    cargo_capacity = db.Column(db.Integer)
    consumables = db.Column(db.String(80))
    cost_in_credits = db.Column(db.Integer)
    crew = db.Column(db.String(80))
    lenght = db.Column(db.Integer)
    manufacturer = db.Column(db.String(80))
    max_speed = db.Column(db.Integer)
    model = db.Column(db.String(80))
    passengers = db.Column(db.String(80))
    vehicle_class = db.Column(db.String(80))
    favorites_vehicles = db.relationship('FavoritesVehicles', backref='vehicle', lazy=True)


    def __repr__(self):
        return '<Vehicle %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "cargo_capacity": self.cargo_capacity,
            "consumables": self.consumables,
            "cost_in_credits": self.cost_in_credits,
            "crew": self.crew,
            "lenght": self.lenght,
            "manufacturer": self.manufacturer,
            "max_speed": self.max_speed,
            "model": self.model,
            "passengers": self.passengers,
            "vehicle_class": self.vehicle_class

            # do not serialize the password, its a security breach
        }  

class FavoritesCharacters(db.Model):
    __tablename__ = 'favorites_characters'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'))



    def __repr__(self):
        return '<FavoritesCharacters %r>' % self.id

    def serialize(self):
        result= Character.query.filter_by(id=self.character_id).first()
        return {
            "id": self.id,
            "name": result.serialize()["name"],
            "user_id": self.user_id

            # do not serialize the password, its a security breach
        } 

class FavoritesPlanets(db.Model):
    __tablename__ = 'favorites_planets'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'))


    def __repr__(self):
        return '<FavoritesPlanets %r>' % self.id

    def serialize(self):
        result= Planet.query.filter_by(id=self.planet_id).first()
        return {
            "id": self.id,
            "name": result.serialize()["name"],
            "user_id": self.user_id

            # do not serialize the password, its a security breach
        } 

class FavoritesVehicles(db.Model):
    __tablename__ = 'favorites_vehicles'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'))


    def __repr__(self):
        return '<FavoritesVehicles %r>' % self.id

    def serialize(self):
        result= Vehicle.query.filter_by(id=self.vehicle_id).first()
        return {
            "id": self.id,
            "name": result.serialize()["name"],
            "user_id": self.user_id

            # do not serialize the password, its a security breach
        }      
    