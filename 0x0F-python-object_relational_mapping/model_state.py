#!/usr/bin/python3
""" This module implements State subclassed by declarative"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """ States class implementation """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
