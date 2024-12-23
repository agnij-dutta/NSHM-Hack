import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your_secret_key_here')
    DATABASE = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'site.db')  # Path to SQLite DB

