from typing import List
from sqlalchemy.orm import Session

from .models import Book

class BookRepository:
    def __init__(self, session: Session):
        self.session = session
    
    def add(self, book: Book) -> Book:
        self.session.add(book)
        self.session.commit()
        self.session.refresh(book)
        return book
    
    def get_by_title(self, title: str) -> Book:
        return self.session.query(Book).filter_by(title=title).first()
    
    def get_all(self) -> List[Book]:
        return self.session.query(Book).all()
    
    def update_summary(self, book: Book, summary: str) -> str:
        book.summary = summary
        self.session.commit()
        return book.summary