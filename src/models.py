import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table user
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    firstname = Column(String(100), nullable=False)
    lastname = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    created_at = Column(DateTime(), default=datetime.now)
    favorites = relationship("Favorite", back_populates="user")
    #Declarar nombre del modelo en la relacion

class Favorite(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    #ForeignKey debe ser definida con el nombre de la tabla y el atributo a usar
    user_id = Column(Integer(), ForeignKey("user.id"), nullable=False)
    favorite_characters = Column(Integer, ForeignKey("character.id"))
    favorite_planets = Column(Integer, ForeignKey("planet.id"))
    favorite_vehicles = Column(Integer, ForeignKey("vehicle.id"))
    user = relationship("User", back_populates="favorites")
    character = relationship("Characters", back_populates="favorites")
    planet = relationship("Planets", back_populates="favorites")
    vehicle = relationship("Vehicles", back_populates="favorites")


class Characters(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    homeworld = Column(Integer, ForeignKey("planet.id"), nullable=False)
    birth_year = Column(Integer, nullable=False)
    height = Column(Integer, nullable=False)
    weight = Column(Integer, nullable=False)
    hair_color = Column(String, nullable=False)
    eye_color = Column(String, nullable=False)
    planet_relationship = relationship("Planets", back_populates="character")
    favorite = relationship("Favorite", back_populates="character")

class Planets(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)
    gravity = Column(Integer, nullable=False)
    population = Column(Integer, nullable=False)
    orbital_period = Column(Integer, nullable=False)
    character_relationship = relationship("Characters", back_populates="planet")
    favorite = relationship("Favorite", back_populates="planet")


class Vehicles(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    max_passengers = Column(Integer, nullable=False)
    cost_in_credits = Column(Integer, nullable=False)
    max_speed = Column(Integer)
    favorite = relationship("Favorite", back_populates="vehicle")

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
