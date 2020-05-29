
import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
