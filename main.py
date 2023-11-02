import os
from database.init_db import db
from database.users import create_user, create_user_table
from handlers.admin import admin_handler
from handlers.command import command_handler
from handlers.message import message_handler
from handlers.callback_query import callback_query_handler
from methods.auth import is_valid_user
from methods.unique import get_user_data
from pyrogram import Client
from src import const
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

# app = Client(
#     "sessions/" + const.session_name,
#     api_id=const.api_id, api_hash=const.api_hash,
#     bot_token=const.bot_token
# )
app = Client(
    "sessions/" + const.test_session_name,
    api_id=const.test_api_id, api_hash=const.test_api_hash,
    bot_token=const.test_bot_token
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


@app.on_callback_query()
async def app_callback_handler(client, callback):
    print(client)
    print(callback)
    # debug(message)
    try:
        user_id = callback.from_user.id
    except AttributeError as err:
        print(f"Warning: {err}  \nFile {__name__} \nLine 43 :")
    else:
        try:
            await callback_query_handler(client, callback)
        except Exception as err:
            print(f"Warning: {err}  \nFile {__name__} \nLine 49 :")


@app.on_message()
async def app_message_handler(client, message):
    # client.send_message(5754619101, message.text)
    # client.send_message(5754619101, message.from_user)
    # debug(message)
    try:
        user_id = message.from_user.id
    except AttributeError as err:
        await client.send_messsage(const.valid_users[0], f"Warning 60 line: {err}")
    else:
        try:
            if user_id:
                create_user(user_id)
                user, strings = get_user_data(user_id)
                if message:
                    if is_valid_user(user):
                        await admin_handler(client, message, user, strings)

                    if message.text:
                        try:
                            if message.text[:1] == "/":
                                await command_handler(client, message, user, strings)
                        except UnicodeError:
                            pass
                    await message_handler(client, message, user, strings)
        except Exception as err:
            print("Warning! 78 line: ", err)
            pass


def main():
    print("Connecting to DataBase")
    db.connect()
    create_db()
    print("Connecting to DataBase ✅")
    print("Bot launching ")
    app.run()


if __name__ == '__main__':
    main()

