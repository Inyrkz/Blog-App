from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#flash for flashing messages after a successful registration
#redirect takes the user to a different url after registration
# importing the Flask class from the flask library
# the render_template connects the flask app to the html template in the template folder

app = Flask(__name__) 
#creating an app variable and setting it to be an instance of the class Flask
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

from flaskblog import routes
# we place it down here to avoid circular importation
