from flask import Flask, Blueprint, request
from app.book import book_blueprint
from flask_cors import CORS
from app.database import session

app = Flask(__name__)
CORS(app)

@app.teardown_request
def remove_session(ex=None):
    session.remove()

default = Blueprint('default', __name__)

@default.route('/', methods=["GET"])
def index():
    return "Xsolla Assessment"

app.register_blueprint(default)
app.register_blueprint(book_blueprint)

if __name__ == "__main__":
    
    app.run(debug=True)