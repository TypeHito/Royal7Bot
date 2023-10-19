import os
from database.init_db import db
from database.users import create_user, create_user_table
from handlers.admin import admin_handler
from handlers.command import command_handler
from handlers.message import message_handler
from methods.auth import is_valid_user
from methods.unique import get_user_data
from pyrogram import Client
from src import const
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

app = Client(
    "sessions/" + const.session_name,
    api_id=const.api_id, api_hash=const.api_hash,
    bot_token=const.bot_token
)


def debug(r):
    print("debug: ", r)


def create_db():
    try:
        create_user_table()
    except Exception as err:
        return str(err)
    else:
        return "Create successful!"





@app.on_message()
def app_message_handler(client, message):
    # client.send_message(5754619101, message.text)
    # client.send_message(5754619101, message.from_user)
    # debug(message)
    user_id = message.from_user.id
    if user_id:
        create_user(user_id)
        user, strings = get_user_data(user_id)
        if message:
            if is_valid_user(user):
                admin_handler(client, message, user, strings)

            if message.text:
                try:
                    if message.text[:1] == "/":
                        command_handler(client, message, user, strings)
                except UnicodeError:
                    pass
            message_handler(client, message, user, strings)



db.connect()


if __name__ == '__main__':
    print("Bot launching")
    # app.start()
    # app.send_message(5754619101, create_db())
    # app.stop()
    app.run()

