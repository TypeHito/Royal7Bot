from methods.unique import send_all, send_me
from database.init_db import db

db.connect()

send_all()
