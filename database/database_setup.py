from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from datetime import datetime, date
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
  __tablename__ = 'user'

  id = Column(Integer, primary_key=True)
  name = Column(String(250), nullable=False)
  email = Column(String(250), nullable=False)

  @property
  def serialize(self):
    """Return object data in easily serializeable format"""
    return {
      'id' :self.id,
      'name'  : self.name,
      'email' : self.email
    }


class Submission(Base):
    __tablename__ = 'submission'

    id = Column(Integer, primary_key=True)
    publication_id = Column(Integer)
    filename = Column(String(250), nullable=False)
    is_valid_format = Column(Boolean, default=False)
    format_validation_message = Column(String(50), default='None')
    is_valid_data = Column(Boolean, default=False)
    data_validation_message = Column(String(50), default='None')
    user_id = Column(Integer,ForeignKey('user.id'))
    user = relationship(User)
    
    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
          'id': self.id,
          'publication_id': self.publication_id,
          'filename': self.filename,
          'is_valid_format': self.is_valid_format,
          'format_validation_message': self.format_validation_message,
          'is_valid_data': self.is_valid_data,
          'data_validation_message': self.data_validation_message,
          'user_id': self.user_id
        }



engine = create_engine('sqlite:///gwas_submissions.db')

# Create tables
Base.metadata.create_all(engine)
