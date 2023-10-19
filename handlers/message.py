from models.buttons.menu_keyboards import main_manu
from database import users
from handlers.command import start
from methods.auth import is_valid_user
from methods.unique import is_flood, get_order_count, get_gifts
from src.const import time_out, valid_users, banner
import threading


async def message_handler(client, message, user, strings):
    contact = message.contact
    if user.current_menu == "send_contact":
        if contact:
            phone_number = contact.phone_number
            users.update_phone_number(user.telegram_id, phone_number)
            users.update_current_menu(user.telegram_id, "main_menu")
            if is_valid_user(user):
                await client.send_message(user.telegram_id, strings["login"], reply_markup=main_manu(strings, True))
            else:
                await client.send_message(user.telegram_id, strings["login"], reply_markup=main_manu(strings))
    elif user.phone_number:
        if message.text == strings["main_menu_1"]:
            if is_flood(user, time_out):
                threading.Thread(target=get_order_count, args=(client, user, strings)).start()
        elif message.text == strings["main_menu_2"]:
            await get_gifts(client, user.telegram_id)
        elif message.text == strings["main_menu_3"]:
            await client.send_photo(user.telegram_id, banner, strings["gifts"])
    else:
        await start(client, user, strings)

