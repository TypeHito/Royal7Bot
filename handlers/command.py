from models.buttons.menu_keyboards import main_manu, request_contact_button
from database.users import update_current_menu
from methods.unique import get_order_count, get_gifts, is_flood
from methods.auth import is_valid_user
import threading
from src.const import banner, time_out


def start(client, user, strings):
    if user.phone_number:
        if is_valid_user(user):
            client.send_message(user.telegram_id, strings["login"], reply_markup=main_manu(strings, True))
        else:
            client.send_message(user.telegram_id, strings["login"], reply_markup=main_manu(strings))
        update_current_menu(user.telegram_id, "main_menu")
    else:
        client.send_message(user.telegram_id, strings["welcome_text"])
        client.send_message(user.telegram_id, strings['please_send_phone_number'],
                     reply_markup=request_contact_button(strings["send_number"]))
        update_current_menu(user.telegram_id, "send_contact")


def command_handler(client, msg, user, strings):
    if msg.text:
        if msg.text == "/start":
            start(client, user, strings)
        if msg.text == "/get_id":
            client.send_message(user.telegram_id, user.telegram_id)
        elif msg.text == "/imkoniyatlar":
            if is_flood(user, time_out):
                threading.Thread(target=get_order_count, args=(client, user, strings)).start()
        elif msg.text == "/sovrinlar":
            get_gifts(client, user.telegram_id)
        elif msg.text == "/aksiya":
            client.send_photo(user.telegram_id, banner, strings["gifts"])



