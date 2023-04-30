from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from app.base import Base


# Create engines and sessions for each Base
engine = create_engine('sqlite:///xsolla.db')
Base.metadata.create_all(bind=engine)
session = scoped_session(sessionmaker(bind=engine))