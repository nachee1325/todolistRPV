from flask import Flask
import database

app = Flask(__name__)
database.connect_to_db()

from app import views