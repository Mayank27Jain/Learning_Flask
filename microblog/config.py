import os

# file for general config across whole app
class Config:
    # SECRET_KEY used to protect against CSRF attacks
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'