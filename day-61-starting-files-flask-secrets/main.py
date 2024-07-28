from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap5
import secrets

# Ideally, this should be in the .env rotate keys
SECRET_KEY = secrets.token_hex(32) # Generates a random 32-byte hex string

class LoginForm(FlaskForm):
    # Validators ensure the user inputs correct data format
    # remember to pip install email_validator
    email = StringField(label='Email', validators=[DataRequired(message="Email is required."), Email(message="Invalid email address")])
    password = StringField(label='Password', validators=[DataRequired(message="Password is required."), Length(min=8, message="Password must be at least 8 characters long")])
    submit = SubmitField(label='Log in')

app = Flask(__name__)
app.secret_key = SECRET_KEY
bootstrap = Bootstrap5(app)

@app.route('/')
def home():
    return render_template('index.html')

# Ensure this route exists if you are trying to access it
@app.route('/login', methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        # Validate email and password
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template('old_WTFORM_login.html', form=login_form)

if __name__ == '__main__':
    app.run(debug=True)
