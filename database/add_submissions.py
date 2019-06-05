#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Submission, User
from datetime import datetime, date
 
engine = create_engine('sqlite:///gwas_submissions.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Check existing db content
allUsers = session.query(User.name).all()
print allUsers

allSubmissions = session.query(Submission.publication_id).all()
print allSubmissions


# IMPORTANT -- Drop tables in case columns have changed during development  
#Base.metadata.drop_all(engine)

# Clear database tables - City, Event, User
session.query(User).delete()
session.query(Submission).delete()
session.commit()


# Create initial user for adding data
User1 = User(name="Laura Harris", email="ljwh@ebi.ac.uk")
session.add(User1)
session.commit()
print User1.name

User2 = User(name="Elliot Solliot", email="eks@ebi.ac.uk")
session.add(User2)
session.commit()
print User2.name

User3 = User(name="Annalisa Buniello", email="buniello@ebi.ac.uk")
session.add(User3)
session.commit()
print User3.name

User4 = User(name="Peggy Hall", email="Peggy.Hall@nih.gov")
session.add(User4)
session.commit()
print User4.name

User5 = User(name="Jackie MacArthur", email="jalm@ebi.ac.uk")
session.add(User5)
session.commit()
print User5.name

User6 = User(name="Lizzy Lewis", email="earl@ebi.ac.uk")
session.add(User6)
session.commit()
print User6.name

User7 = User(name="Maria Cerezo", email="mcerezo@ebi.ac.uk")
session.add(User7)
session.commit()
print User7.name

User8 = User(name="Test User", email="someone@ebi.ac.uk")
session.add(User8)
session.commit()
print User8.name

User9 = User(name="Aoife McMahon", email="aoifem@ebi.ac.uk")
session.add(User9)
session.commit()
print User9.name

User10 = User(name="Joannella Morales", email="jmorales@ebi.ac.uk")
session.add(User10)
session.commit()
print User10.name


# Submission info
submission1 = Submission(publication_id=12334, filename='', is_valid_format=0, is_valid_data=0, user_id=1)
session.add(submission1)
session.commit()

submission2 = Submission(publication_id=1122, filename='', is_valid_format=0, is_valid_data=0, user_id=1)
session.add(submission2)
session.commit()

submission3 = Submission(publication_id=5678, filename='', is_valid_format=0, is_valid_data=0, user_id=2)
session.add(submission3)
session.commit()




# Debug statements to confirm data entry
print "Added submissions and users!"
allSubmissions = session.query(Submission).all()
print "Added ", len(allSubmissions), " submissions"



