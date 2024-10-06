from sqlalchemy import Column, Integer, String, Text, JSON, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
DATABASE_URI = 'sqlite:///job_recommendation.db'

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    skills = Column(JSON)  # List of skills
    experience_level = Column(String)
    preferences = Column(JSON)  # Preferences as JSON

class JobPosting(Base):
    __tablename__ = 'job_postings'
    id = Column(Integer, primary_key=True)
    job_title = Column(String)
    company = Column(String)
    required_skills = Column(JSON)
    location = Column(String)
    job_type = Column(String)
    experience_level = Column(String)

# Set up the database
engine = create_engine(DATABASE_URI)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
