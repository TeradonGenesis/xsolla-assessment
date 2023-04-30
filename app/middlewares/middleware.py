from flask import request, jsonify
from functools import wraps

def check_book_post_json_request(view_func):
    @wraps(view_func)
    def wrapper(*args, **kwargs):    
        required = ['title']
        missing = [param for param in required if param not in request.json]
        if missing and request.method in ['POST']:
            return jsonify({'error':f'Missing request parameters: {missing}'}), 400
        return view_func(*args, **kwargs)
    
    return wrapper

def check_upload_book_request(view_func):
    @wraps(view_func)
    def wrapper(*args, **kwargs):    
        required = ['file']
        missing = [param for param in required if param not in request.files]
        if missing and request.method in ['POST']:
            return jsonify({'error':f'Missing request parameters: {missing}'}), 400
        return view_func(*args, **kwargs)
    
    return wrapper
    