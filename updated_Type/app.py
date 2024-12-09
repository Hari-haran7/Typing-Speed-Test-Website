from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///typing_test.db'
db = SQLAlchemy(app)

# Database models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    history = db.relationship('TypingHistory', backref='user', lazy=True)

class TypingHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    wpm = db.Column(db.Integer, nullable=False)
    mistakes = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password)

        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! You can now log in.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            return redirect(url_for('index'))

        flash('Invalid username or password', 'danger')

    return render_template('login.html')

@app.route('/index', methods=['GET'])
def index():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('index.html')

@app.route('/submit_test', methods=['POST'])
def submit_test():
    if 'user_id' in session:
        wpm = request.form['wpm']
        mistakes = request.form['mistakes']

        new_entry = TypingHistory(user_id=session['user_id'], wpm=wpm, mistakes=mistakes)
        db.session.add(new_entry)
        db.session.commit()

    return redirect(url_for('index'))

@app.route('/test_history', methods=['GET'])
def test_history():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    user_history = TypingHistory.query.filter_by(user_id=session['user_id']).all()
    
    # Convert timestamps to IST and format them
    for entry in user_history:
        # Convert timestamp to IST
        entry.timestamp = entry.timestamp + timedelta(hours=5, minutes=30)
        # Round off the timestamp to hh:mm:ss format
        entry.timestamp = entry.timestamp.strftime("%Y-%m-%d %H:%M:%S")

    return render_template('test_history.html', history=user_history)

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
