from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
#O app utilizou os seguintes modulos flask, flask-login, flask-sqlalchemy