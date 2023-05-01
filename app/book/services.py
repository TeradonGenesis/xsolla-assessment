from langchain import OpenAI, PromptTemplate
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain
from langchain.document_loaders import PyPDFLoader
import openai
from typing import List

from .models import Book
from .repositories import BookRepository

class BookService:
    def __init__(self, book_repository: BookRepository, api_key: str):
        self.book_repository = book_repository
        self.llm = OpenAI(temperature=0, openai_api_key=api_key)
        self.text_splitter = CharacterTextSplitter()
        openai.api_key = api_key
    
    def create_book(self, title: str, contentType: str, content: str = None) -> Book:
        book = Book(title=title, content=content, contentType=contentType)
        self.book_repository.add(book)
        return book
    
    def get_book_by_title(self, title: str) -> Book:
        return self.book_repository.get_by_title(title)
    
    def get_all_books(self) -> List[Book]:
        return self.book_repository.get_all()
    
    def update_summary(self, book: Book, summary: str) -> str:
        return self.book_repository.update_summary(book, summary)
    
    def generate_summary_from_pdf(self, file_path: str) -> str:
        loader = PyPDFLoader(file_path)
        docs = loader.load_and_split()
        chain = load_summarize_chain(self.llm, chain_type="map_reduce")
        summary = chain.run(docs)
        return summary
    
    def generate_summary_from_content(self, book_content: str) ->str:
        try:
            prompt = f"Please summarize the following book content: {book_content}"
            
            response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", 
            messages = [
                    {"role": "system", "content" : "You are BookSummarizerGPT, you are going to summarize the book content"},
                    {"role": "user", "content" : prompt},
                ]
            )
            
            summary = response.choices[0].message.content
    
            return summary
        except Exception as e:
            print(f"Error generating summary: {str(e)}")
            return None
        
    def check_allow_extension(self, filename: str, allowed_ext: List[str]) -> bool:
        return '.' in filename and filename.rsplit('.',1)[1].lower() in allowed_ext
    
    def split_extension(self, filename: str) -> List[str]:
        return filename.rsplit('.',1)
