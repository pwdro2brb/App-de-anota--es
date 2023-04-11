from flask import Blueprint

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return "<h1> TESTE DE um COMEÇO de UMA vida <h1>"