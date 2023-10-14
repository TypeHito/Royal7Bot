from methods.hive import ANDIJON, FARGONA
from database.users import update_order_count
from methods.telegram_bot.bot_answer import send_message, send_photo, edit_message_text
from database.users import update_last_sms, get_user
from core.const import time_out
import datetime
from methods.telegram_bot.result_models import User
from lang.language_handler import load_lang
from database.users import create_user
from core.const import photo, text
from database.users import get_all_users_id
from core.const import valid_users
from models.video_text_button import video_content_r7
import threading
import time


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


def get_order_count(user, strings):
    message_status = send_message(user.telegram_id, strings["loading_chance"])
    result = message_status.get("result")
    if result:
        message_id = result.get("message_id")
        if is_flood(user, time_out):
            andijan = ANDIJON.get_count(user.phone_number)
            fargona = FARGONA.get_count(user.phone_number)
            if andijan is False or fargona is False:
                edit_message_text(user.telegram_id, strings["server_error"], message_id)
                return
            count = ANDIJON.get_count(user.phone_number) + FARGONA.get_count(user.phone_number)
            if int(count) < 7:
                edit_message_text(user.telegram_id, strings["need_more_chance"].format(7 - count), message_id)
            else:
                edit_message_text(user.telegram_id, strings["you_have_chance"].format(count - 6), message_id)
            update_order_count(user.telegram_id, count)


def get_gifts(chat_id, strings):
    for i in range(7):
        send_photo(chat_id, photo[i], text[i])


def get_user_data(telegram_id):
    data = get_user(telegram_id)
    if data:
        user = User(*data)
        strings = load_lang(user.language)
    else:
        create_user(telegram_id)
        return get_user_data(telegram_id)
    return user, strings


def send_me():
    users = get_all_users_id()
    count = 0
    send_message(valid_users[0], "Start Posting")
    video_content_r7(valid_users[0])
    # threading.Thread(target=video_content_r7, args=valid_users[0]).start()
    for i in users:
        # video_content_r7(v)
        # threading.Thread(target=video_content_r7, args=valid_users[0]).start()
        count += 1
        if count % 1000 == 0:
            send_message(valid_users[0], f"Post message count: {count}")
            time.sleep(1)
    send_message(valid_users[0], "End Posting")


def send_all():
    users = get_all_users_id()
    count = 0
    thread = 0
    # for i in valid_users:
    #     send_message(i, f"Start Posting: {len(users)}")
    for user in users:
        if thread > 10:
            thread += 1
        if count > 29000:
            print(video_content_r7(user[0]))
        # threading.Thread(target=video_content_r7, args=user[0]).start()
        count += 1
        if count % 1000 == 0:
            for i in valid_users:
                send_message(i, f"Sended message count: {count}")
    for i in valid_users:
        send_message(i, "End Posting!")