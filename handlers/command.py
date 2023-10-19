from models.buttons.menu_keyboards import main_manu, request_contact_button
from database.users import update_current_menu
from methods.unique import get_order_count, get_gifts, is_flood
from methods.auth import is_valid_user
import threading
from src.const import banner, time_out


async def start(client, user, strings):
    if user.phone_number:
        if is_valid_user(user):
            await client.send_message(user.telegram_id, strings["login"], reply_markup=main_manu(strings, True))
        else:
            await client.send_message(user.telegram_id, strings["login"], reply_markup=main_manu(strings))
        update_current_menu(user.telegram_id, "main_menu")
    else:
        await client.send_message(user.telegram_id, strings["welcome_text"])
        await client.send_message(user.telegram_id, strings['please_send_phone_number'],
                     reply_markup=request_contact_button(strings["send_number"]))
        update_current_menu(user.telegram_id, "send_contact")


async def command_handler(client, msg, user, strings):
    if msg.text:
        if msg.text == "/start":
            await start(client, user, strings)
        if msg.text == "/get_id":
            await client.send_message(user.telegram_id, user.telegram_id)
        elif msg.text == "/imkoniyatlar":
            if is_flood(user, time_out):
                threading.Thread(target=get_order_count, args=(client, user, strings)).start()
        elif msg.text == "/sovrinlar":
            await get_gifts(client, user.telegram_id)
        elif msg.text == "/aksiya":
            await client.send_photo(user.telegram_id, banner, strings["gifts"])



