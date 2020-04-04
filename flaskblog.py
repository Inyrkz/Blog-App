from datetime import datetime # importing datetime class from datetime library
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
#flash for flashing messages after a successful registration
#redirect takes the user to a different url after registration
# importing the Flask class from the flask library
# the render_template connects the flask app to the html template in the template folder


app = Flask(__name__) #creating an app variable and setting it to be an instance of the class Flask
#The double underscore name is a special variable in python. It is just the name of the module.
#It helps flask know where to look for static files and templates'''

#setting secret key to protect against modifying cookies and cross-site request forgery attacks
app.config['SECRET_KEY'] = '8231c6aa677ca2ae38e9860b7e27819c'
#In command line(python interpreter), import secrets
#secrets.token_hex(16)
#exit()

# we don't have a database file, so let's create one
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
#the /// means that the site.db file should be created in our project folder along side our python module that we are currently in 

#creating the database instance
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False) #Unique=True means the value must be unique
    email = db.Column(db.String(120), unique=True, nullable=False) #nullable=False means a value must be inserted, it must not be null
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg') # there must be a default profile picture for each user
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy='True')
    # one to many relationship of user to post, 'Post' means the posts has a relationship to our post model
    # backref is similar to adding another column to the post model, when we have a post, the backref allows us to use the 'author' attribute to see who created the post
    # the 'lazy' just defines when SQL Alchemy loads the data from the database, so 'true' means SQL Alchemy will load the data as necessary in one go.
    # the posts variable is not a column in the database, it's kindoff an additional query in the background that will get all the posts the user has created

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"
        # magic methods, how object is printed, when we print it out.

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow) #no bracket added after the datetime.utcnow so it wont use the current time as at the creation of this app as default time
    #always use utc when saving date and time to a database
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    #user.id is in lower case because we are referencing a table in the User class, not the class itself as we did with Post in the posts variable

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"


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


if __name__ == '__main__':
    app.run(debug=True) #running in debug mode so any changes in the code wil reflect on the browser when it is refreshed.
