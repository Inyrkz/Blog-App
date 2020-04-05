from datetime import datetime # importing datetime class from datetime library
from flaskblog import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False) #Unique=True means the value must be unique
    email = db.Column(db.String(120), unique=True, nullable=False) #nullable=False means a value must be inserted, it must not be null
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg') # there must be a default profile picture for each user
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy='dynamic')
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
