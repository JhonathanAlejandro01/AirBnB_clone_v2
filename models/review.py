#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship, backref
from os import getenv

class Review(BaseModel, Base):
    """ Review classto store review information """

    __tablename__ = "reviews"
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey("places.id", ondelete="CASCADE"), nullable=False)
    user_id = Column(String(60),ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    