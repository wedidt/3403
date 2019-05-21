## Introduction

This project is runned on python and Flask.
Use Flask-Sqlalchemy for Database ORM


## Modules required

flask package
flask-sqlalchemy
booststrap
jinja2
werkzeug


## How to run

At the folder base directory open the ubuntu cmd line and run:
1) python3 -m venv venv
2) source /venv/bin/activate
3) pip install flask
4) pip install flask-sqlalchemy
5) FLASK_APP=app.py
6) flask run
7) run https://localhost:5000/init_db on browser
8) run https://localhost:5000/

## How to use the website

# Home
Shows the rank of movies and the ability to vote them

# Dashboard
Choose between User Manager or Movie Manager

# User Manager
Create or delete users

# Movie Manager
Create or delete movies

# Register
Register as a new user

# Log In
Log in the website using existing account


## Reference

Movie List https://www.imdb.com
SQLAlchemy: http://flask.pocoo.org/docs/1.0/quickstart/
Chart.js: https://www.chartjs.org/
Flask tutorial: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world