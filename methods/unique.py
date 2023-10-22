from methods.hive import ANDIJON, FARGONA
from methods.language import load_lang
from models.UserModel import User
from database.users import update_order_count, update_last_sms, create_user, get_user
from src.const import action_photo, action_text, time_out
import datetime


def is_flood(user, in_time_out):
    now = datetime.datetime.now()
    if user.last_sms:
        time_left = now - user.last_sms
        if time_left > datetime.timedelta(seconds=in_time_out) or not user.last_sms:
            update_last_sms(user.telegram_id, now)
            return True
        return False
    else:
        update_last_sms(user.telegram_id, now)
        return True


def get_order_count(client, user, strings):
    message_status = client.send_message(user.telegram_id, strings["loading_chance"])
    if message_status:
        message_id = message_status.id
        if is_flood(user, time_out):
            andijan = ANDIJON.get_count(user.phone_number)
            fargona = FARGONA.get_count(user.phone_number)
            if andijan is False or fargona is False:
                client.edit_message_text(user.telegram_id, message_id, strings["server_error"])
                return
            count = ANDIJON.get_count(user.phone_number) + FARGONA.get_count(user.phone_number)
            if int(count) < 7:
                client.edit_message_text(user.telegram_id, message_id, strings["need_more_chance"].format(7 - count))
            else:
                client.edit_message_text(user.telegram_id, message_id, strings["you_have_chance"].format(count - 6))
            update_order_count(user.telegram_id, count)


async def get_gifts(client, chat_id):
    for i in range(7):
        await client.send_photo(chat_id, action_photo[i], action_text[i])


def get_user_data(telegram_id):
    data = get_user(telegram_id)
    if data:
        user = User(*data)
        strings = load_lang(user.language)
    else:
        create_user(telegram_id)
        return get_user_data(telegram_id)
    return user, strings
