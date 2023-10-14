from methods.telegram_bot.bot_answer import send_message, send_photo
from buttons.menu_keyboards import main_manu
from database import users
from handlers.command import start
from methods.auth import is_valid_user
from methods.unique import is_flood, get_order_count, get_gifts
from core.const import time_out, valid_users, banner
import threading


def message_handler(msg, user, strings):
    contact = msg.contact[0]

    if user.current_menu == "send_contact":
        if contact:
            phone_number = contact["phone_number"]
            users.update_phone_number(user.telegram_id, phone_number)
            users.update_current_menu(user.telegram_id, "main_menu")
            if is_valid_user(user):
                send_message(user.telegram_id, strings["login"], reply_markup=main_manu(strings, True))
            else:
                send_message(user.telegram_id, strings["login"], reply_markup=main_manu(strings))
            return
    elif user.phone_number:
        if msg.text == strings["main_menu_1"]:
            if is_flood(user, time_out):
                threading.Thread(target=get_order_count, args=(user, strings)).start()
        elif msg.text == strings["main_menu_2"]:
            get_gifts(user.telegram_id, strings)
        elif msg.text == strings["main_menu_3"]:
            req = send_photo(user.telegram_id, banner, strings["gifts"])
            if not req['ok']:
                send_message(valid_users[0], "Error: " + str(req))
        return
    start(user, strings)

