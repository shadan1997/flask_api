# routes.py

from flask import Blueprint, request
from controllers import obj
from routes import *

api = Blueprint('api', __name__)

#http://127.0.0.1:5000/say_hi
@api.route('/say_hi', methods=['GET'])
def get_hi():
    return obj.say_hi()

#http://127.0.0.1:5000/say_hi_to?name=parvez
@api.route('/say_hi_to', methods=['GET'])
def example():
    name = request.args.get('name')
    if name:
        return obj.say_hi_to(name)
    
#... add here