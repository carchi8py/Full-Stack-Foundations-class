from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from puppies import Base, Shelter, Puppy
from pprint import pprint

import datetime

engine = create_engine('sqlite:///puppyshelter.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
print 'hi'

puppies = session.query(Puppy).order_by(Puppy.name).all()
for puppy in puppies:
	print puppy.name

sixMonthOld = (datetime.date.today() - datetime.timedelta(6*365/12)).isoformat()

puppies = session.query(Puppy).filter(Puppy.dateOfBirth > sixMonthOld)
for puppy in puppies:
	print puppy.name
	print puppy.dateOfBirth
	print "\n"

puppies = session.query(Puppy).order_by(Puppy.weight).all()
for puppy in puppies:
	print puppy.name
	print puppy.weight
	print "\n"

puppies = session.query(Puppy).order_by(Puppy.shelter_id).all()
for puppy in puppies:
	print puppy.name, puppy.shelter.name