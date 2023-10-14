from flask import Flask, request
from flask_sslify import SSLify

# constants
from methods.telegram_bot.result_models import Message

# methods
from methods.telegram_bot.init_methods import get_user_id
from database.users import create_user, create_user_table


# handlers
from handlers.admin import admin_handler
from handlers.command import command_handler
from handlers.message import message_handler
from handlers.callback_query import callback_query_handler
from methods.auth import is_valid_user
from methods.unique import get_user_data

app = Flask(__name__)
sslify = SSLify(app)


def debug(r):
    print("debug: ", r)


@app.get("/create_db")
def create_db():
    try:
        create_user_table()
    except Exception as err:
        return str(err)
    else:
        return "Create successful!"


@app.post("/bot")
def index():
    response = request.get_json()
    debug(response)

    user_id = get_user_id(response)
    message = response.get("message")
    callback_query = response.get("callback_query")
    if user_id:
        create_user(user_id)
        user, strings = get_user_data(user_id)

        if message:
            msg = Message(**message)
            if is_valid_user(user):
                admin_handler(msg, user, strings)
            if msg.text:
                if msg.text[:1] == "/":
                    command_handler(msg, user, strings)
                    return {"ok": True}

            message_handler(msg, user, strings)
        elif callback_query:
            callback_query_handler(callback_query)
            return {"ok": True}
    return {"ok": False}
