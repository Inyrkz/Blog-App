from flaskblog import app # imports from the __init__.py file within the flaskblog package

if __name__ == '__main__':
    app.run(debug=True) #running in debug mode so any changes in the code wil reflect on the browser when it is refreshed.
