from flask import *
from dotenv import load_dotenv, find_dotenv
import os
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

load_dotenv(find_dotenv(".env"))

app = Flask(__name__)
app.secret_key = "my secret"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'index'

@login_manager.user_loader
def load_user(username):
    return Person.query.get(int(username))

class Person(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)


with app.app_context():
    db.create_all()
@app.route('/favicon.ico')
def favicon():
    return send_from_directory('./static/images', 'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = Person.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            flash('Login successful.', 'success')
            return redirect(url_for('home'))

        flash('Invalid username or password. Please try again.', 'error')

    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        try:
            username = request.form['username']
            password = request.form['password']
            confirm_password = request.form['confirm-password']

            # Check if username is already taken
            if Person.query.filter_by(username=username).first():
                flash('Username already taken. Please choose a different one.', 'error')
                return redirect(url_for('register'))

            # Check if passwords match
            if password != confirm_password:
                flash('Passwords do not match. Please try again.', 'error')
                return redirect(url_for('register'))

            # Create a new user
            new_user = Person(username=username, password=generate_password_hash(password, method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()

            flash('Registration successful. You can now log in.', 'success')
            return redirect(url_for('home'))

        except Exception as e:
            flash('An error occurred. Please try again later.', 'error')
            print(f"Error: {e}")

    return render_template('register.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("index"))

@app.route('/home')
@login_required
def home():
    return render_template('home.html')

@app.route('/about')
@login_required
def about():
    return render_template('about.html')

@app.route('/services')
@login_required
def services():
    return render_template('services.html')

@app.route('/contact')
@login_required
def contact():
    return render_template('contact.html')


