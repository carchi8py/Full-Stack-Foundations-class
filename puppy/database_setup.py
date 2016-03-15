import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Shelter(Base):
	__tablename__ = 'shelter'
	name = Column(String(80), nullable = False)
	id = Column(Integer, primary_key = True)
	address = Column(String(250))
	city = Column(String(80))
	state = Column(String(80))
	zipCode = Column(Integer)
	website = Column(String(250))

class Puppy(Base):
	__tablename__ = 'puppy'
	name = Column(String(80), nullable = False)
	shelter_id = Column(Integer, primary_key = True)
	dateOfBirth = Column(Date)
	gender = Column(String(80))
	weight = = Column(Integer)

engine = create_engine('sqlite:///puppies.db')
Base.metadata.create_all(engine)