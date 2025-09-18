from flask import Flask, render_template, redirect, flash
from forms import LoginForm, SignupForm

app = Flask(__name__)

app.config.from_object('default_config')
app.config.from_prefixed_env()

@app.route('/')
def index_ep():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login_ep():
    form = LoginForm()

    if form.validate_on_submit():
        flash('You are logged in.')
        return redirect('/')

    return render_template('login.html', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup_ep():
    form = SignupForm()

    if form.validate_on_submit():
        flash('You are now signed up.')
        return redirect('/')

    return render_template('signup.html', form=form)
