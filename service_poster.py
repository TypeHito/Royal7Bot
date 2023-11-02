from methods.poster import send_post
from database.users import get_all_users_id
from database.init_db import db
from handlers.callback_query import callback_query_handler
from src import const
from pyrogram import Client
from models.buttons import menu_keyboards
import asyncio
#

# app = Client(
#     "sessions/" + const.test_session_name,
#     api_id=const.test_api_id, api_hash=const.test_api_hash,
#     bot_token=const.test_bot_token
# )
app = Client(
    "sessions/" + const.session_name,
    api_id=const.api_id, api_hash=const.api_hash,
    bot_token=const.bot_token
)
db.connect()
button = menu_keyboards.get_start("🗝 Imkonyatlarni tekshirish", "🔄Botni yangilash")

# all = get_all_users_id()
# print(len(get_all_users_id()))
app.start()
send_post(app, get_all_users_id(),  "photo", const.last_post_text, const.last_post, button)
# send_post(app, const.valid_users,  "photo", const.last_post_text, const.last_post, button)
app.stop()

