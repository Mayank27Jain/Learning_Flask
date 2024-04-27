from flask import render_template, flash, redirect, url_for
from app import app
# the variable from the package
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', user=user, posts=posts) # Uses Jinja template engine on ./templates/index.html

# the default is to only accept GET requests
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    # below method returns false if sent by GET, and true if fields are correctly sent by POST
    if form.validate_on_submit():
        # the flash function throws a message to be displayed. We do this in the base.html
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        # redirect instructs browser to jump to a different URL
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)