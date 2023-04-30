from flask import Blueprint

book_blueprint = Blueprint('book', __name__, url_prefix='/api/books')

from . import views