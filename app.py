from flask import Flask, render_template, request, redirect, abort, url_for, session
from database import init_db, db_session
from models import User, Movie

app = Flask("MovieRanking")
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/')
def index():
    movies = Movie.query.all()

    movie_votes = ','.join(str(movie.vote) for movie in movies)

    movie_names = '\'' + "','".join(movie.name for movie in movies) + '\''

    return render_template("index.html", title="Home", movies=movies, movie_names=movie_names, movie_votes=movie_votes)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        return do_login(request.form["email"], request.form["password"])

    return render_template('login.html', title="Log In")


def do_login(email, password):
    user = User.query.filter(User.email == email).first()

    if user == None:
        return render_template('login.html', title="Log In", errors=["Account not found."])

    if user.password != password:
        return render_template('login.html', title="Log In", errors=["Wrong password."])

    session['username'] = user.email

    return redirect(url_for('index'))


@app.route('/logout')
def logout():
    session.pop('username', None)

    return redirect(url_for('index'))


@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return abort(401)

    return render_template('dashboard.html', title="Dashboard")


@app.route('/dashboard/movie', methods=["GET", "POST"])
def movie():
    if request.method == "POST":
        return do_create_movie(request.form)

    movies = Movie.query.all()

    return render_template('movie_manager.html', title="Movie Manager", movies=movies)


def do_create_movie(form):
    movie = Movie(name=form["name"], info=form["info"])

    db_session.add(movie)
    db_session.commit()

    return redirect(url_for("movie"))


@app.route('/dashboard/delete_movie', methods=["POST"])
def delete_movie():
    movie = Movie.query.filter(Movie.id == request.form["id"]).first()

    db_session.delete(movie)
    db_session.commit()
    return redirect(url_for("movie"))


@app.route('/dashboard/user', methods=["GET", "POST"])
def user():
    if request.method == "POST":
        return do_create_user(request.form)

    users = User.query.all()

    return render_template('user_manager.html', title="User Manager", users=users)


def do_create_user(form):
    user = User(email=form["email"], password=form["password"])

    db_session.add(user)
    db_session.commit()

    return redirect(url_for("user"))


@app.route('/dashboard/delete_user', methods=["POST"])
def delete_user():
    user = User.query.filter(User.id == request.form["id"]).first()

    db_session.delete(user)
    db_session.commit()
    return redirect(url_for("user"))


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        return do_register(request.form["email"], request.form['password'])
    else:
        return render_template('register.html', title="Register")


def do_register(email, password):
    user = User(email=email, password=password)

    try:
        db_session.add(user)
        db_session.commit()
    except:
        return render_template('register.html', title="Register", errors=["This email is already in use."], email=email)
    return redirect(url_for('login'))


@app.route('/like_movie', methods=["POST"])
def like_movie():
    movie = Movie.query.get(request.form["id"])
    movie.vote = movie.vote + 1

    db_session.commit()

    return redirect(url_for('index'))


@app.route('/init_db')
def do_init_db():
    init_db()

    return "Init Database Finished."


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
