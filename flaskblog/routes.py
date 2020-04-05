from flask import render_template, url_for, flash, redirect
from flaskblog.forms import RegistrationForm, LoginForm 
from flaskblog.models import User, Post
# now that we are in a package we import from the package name then the module name
from flaskblog import app # for our decorators @app

my_posts = [
    {
        'author': 'Samuel Umoren',
        'title': 'The art of being a fool',
        'content': 'A cool soundcloud mix',
        'date_posted': 'October 6, 2019'
    },
    {
        'author': 'Aniekeme Udoetuk',
        'title': 'How to stop masturbating',
        'content': 'Explicit content',
        'date_posted': 'August 3, 2018' 
    }, 
    {
        'author': 'Ini-Abasi Bernard',
        'title': 'Green Lanterns on Earth',
        'content': 'Willpower',
        'date_posted': 'April 21, 2018' 
    }
] # created a dummy variable of a list of dictionaries for our blog

@app.route("/") #what we type in our browser to go to different pages. This is a decorator.
def hello():
    return render_template('home.html', posts=my_posts)
    # we will have access to the variable passed through the 'posts' argument

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm() #creating an instance of the class
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success') #using an f sting since we are gonna pass in a variable
        return redirect(url_for('hello')) # redirect after successful registration to homepage using hello function
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm() #creating an instance of the class
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success' )
            return redirect(url_for('hello'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger' )
    return render_template('login.html', title='Login', form=form)
