# __init__.py: executed when the app module is imported
from flask import Flask

app = Flask(__name__) # this is a variable, using __name__ should work 99% of the time

from app import routes # this import from the package named app which we are building now
# the routes module needs to import the app variable, and we want to avoid circular imports