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
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('O email tem que ser maior que 3 cracteres', category='error')
        elif len(first_name) < 2:
            flash('O nome tem que ser maior que 1 cracteres', category='error')
        elif password1 != password2:
            flash('Senhas diferentes', category='error')
        elif len(password1) < 7:
            flash('A senha tem que ser maior que 7 cracteres', category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(
                password1, method='sha256'))
            db.session.add(new_user)
            flash('Conta criada!!!', category='success')
            return redirect(url_for('views.home'))
           #adiciona o usuário no banco de dados
           
    
    return render_template("sign-up.html")

