from flask import request, jsonify
from . import book_blueprint
from .repositories import BookRepository
from .services import BookService
import os
from app import database
from werkzeug.utils import secure_filename
from app.middlewares.middleware import check_book_post_json_request, check_upload_book_request
from dotenv import load_dotenv

load_dotenv()
book_repository = BookRepository(database.session)
book_service = BookService(book_repository, os.environ.get('OPENAI_API_KEY'))

@book_blueprint.route('/',methods=["GET"])
def get_books():
    try:
        title = request.args.get('title')
        
        if title:
            book = book_service.get_book_by_title(title)
            
            if book is None:
                raise Exception(f'Book {title} does not exist')
            
            return jsonify({
                'id': book.id,
                'title': book.title,
                'content': book.content,
                'summary': book.summary,
                'type': book.contentType
            }), 200
        else:
            book_list = []

            books = book_service.get_all_books()
            if books:
                for book in books:
                    book_list.append({
                        'id': book.id,
                        'title': book.title,
                        'content': book.content,
                        'summary': book.summary,
                        'type': book.contentType
                    })
                
            return jsonify({
                'books': book_list
            }), 200
    except Exception as e:
            error_message = str(e)
            return jsonify({"error": error_message}), 400

@book_blueprint.route('/',methods=["POST"])
@check_book_post_json_request
def create_book():
    try:
        if 'content' not in request.json:
            raise Exception('Content parameter is missing')
        
        title = request.json['title']
        content = request.json['content']
        
        if not content:
            raise Exception('Content for the book is empty')
        #check if the book record is created already
        book = book_service.get_book_by_title(title)
        if book:
            raise Exception(f'Cannot create book. {title} already exist')
        
        book = book_service.create_book(title, 'json', content)
        
        return jsonify({
            'message': 'Book is created',
            'id': book.id,
            'title': book.title
        }), 201
        
    except Exception as e:
            error_message = str(e)
            return jsonify({"error": error_message}), 400


@book_blueprint.route('/upload',methods=["POST"])
@check_upload_book_request
def upload_book():
    try:
        file = request.files['file']

        #rename the title if theres spacing
        filename = secure_filename(file.filename)
        
        #check if it a file and file type is pdf
        is_pdf = book_service.check_allow_extension(filename, ['pdf'])
        
        if is_pdf is False:
            raise Exception(f'Cannot upload pdf book. {filename} is not a pdf')
        
        # Set the destination folder
        destination_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'content')

        # Ensure that the destination folder exists
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        # Set the filename and save the file
        filepath = os.path.join(destination_folder, filename)
        
        data = book_service.split_extension(filename)
        
        #check if the book record is created already
        book = book_service.get_book_by_title(data[0])
        if book:
            raise Exception(f'Cannot upload pdf book. {filename} already exist')
        
        created_book = book_service.create_book(data[0], data[1])
        
        if created_book is None:
            raise Exception(f'Cannot upload pdf book. {filename} failed to save')
        
        file.save(filepath)
        
        return jsonify({
            'message': 'Book is uploaded',
            'id': created_book.id,
            'title': created_book.title
        }), 201
        
    except Exception as e:
            error_message = str(e)
            return jsonify({"error": error_message}), 400
        
@book_blueprint.route('/summary',methods=["POST"])
@check_book_post_json_request
def summarize_book():
    try:
        title = request.json['title']
        
        #check if the book record is created already
        book = book_service.get_book_by_title(title)
        if book is None:
            raise Exception(f'Book {title} does not exist')
        
        if book.summary is None:
            generated_summary = ''
            if book.contentType == 'pdf':
                pdf_file = book.title + '.' + book.contentType
                destination_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'content')
                filepath = os.path.join(destination_folder, pdf_file)
                
                if os.path.exists(filepath):
                    generated_summary = book_service.generate_summary_from_pdf(filepath)
                else:
                    raise Exception(f'File does not exist')
                
            elif book.contentType == 'json':
                generated_summary = book_service.generate_summary_from_content(book.content)
            else:
                raise Exception(f'Book with content type {book.contentType} does not support summarization currently')
            
            if generated_summary != '':
                summary = book_service.update_summary(book, generated_summary)
                
        else:
            summary = book.summary
        
        return jsonify({
            'summary': summary
        }), 200
        
    except Exception as e:
            error_message = str(e)
            return jsonify({"error": error_message}), 400
        
        
@book_blueprint.route('/summary',methods=["GET"])
def get_book_summary():
    try:
        title = request.args.get('title')
        
        if title:
            book = book_service.get_book_by_title(title)
            
            if book is None:
                raise Exception(f'Book {title} does not exist')
            
            return jsonify({
                'title': book.title,
                'summary': book.summary,
            }), 200
        else:
            book_list = []

            books = book_service.get_all_books()
            if books:
                for book in books:
                    book_list.append({
                        'title': book.title,
                        'summary': book.summary
                    })
                
            return jsonify({
                'books': book_list
            }), 200
    except Exception as e:
            error_message = str(e)
            return jsonify({"error": error_message}), 400
    