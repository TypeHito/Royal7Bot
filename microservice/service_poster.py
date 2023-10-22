from methods.poster import send_post
# from database.users import get_all_users_id
from src import const
from pyrogram import Client
from models.buttons import menu_keyboards
#
app = Client(
    "../sessions/" + const.test_session_name,
    api_id=const.test_api_id, api_hash=const.test_api_hash,
    bot_token=const.test_bot_token
)
button = menu_keyboards.ok_cancel("ok", "cancel")

app.start()
# all = get_all_users_id()

send_post(app, [(const.valid_users[0],0)],  "photo", "text", const.banner, button)
app.stop()
