from sqlalchemy import Column, Integer, String
from app.base import Base

class Book(Base):
    __tablename__ = 'books'
    
    id = Column(Integer,primary_key=True)
    title = Column(String(255),nullable=False)
    content = Column(String,nullable=True)
    contentType = Column(String(100),nullable=False)
    summary = Column(String,nullable=True)
    
    def __repr__(self):
        return f"<Book(title='{self.title}', summary='{self.summary}')>"
    
        
        
        
        