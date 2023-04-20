from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html", bolean=False)

@auth.route('/logout')
def logout():
    return "<p>Deslogar </p>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('first-name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
               
               
        if len(email) < 4 :
           flash('O email deve conter mais de que 4 caracteres. ', category='error')
        elif len(firstName) < 2:
           flash('O nome deve conter mais de que 1 caracter ', category='error')
        elif password1 != password2:
           flash('As senhas não estão iguais ', category='error')
        elif len(password1) < 7:
           flash('A senha deve conter no mínimo 7 caracteres ', category='error')
        else:
           new_user= User(email=email, firstName=firstName, password=generate_password_hash(password1, method='sha256'))
           db.session.add(new_user)
           db.session.commit()
           
           flash('Conta criada!!!!! ', category='success')
           #adiciona o usuário no banco de dados
           
    
    return render_template("sign-up.html")

