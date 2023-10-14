from methods.telegram_bot.result_models import CallbackQuery
from methods.unique import get_user_data
from methods.unique import is_flood, get_order_count
from methods.telegram_bot.bot_answer import edit_message_text, delete_message
from methods.send_post import re_post
from database.users import get_all_users_id
import datetime
import threading
from database.users import update_stable_id, update_stable_key
from handlers.command import start


def callback_query_handler(callback_data):
    data = CallbackQuery(**callback_data)
    try:
        command, params = str(data.data).split('_')
    except ValueError:
        command = data.data
    chat_id = callback_data['from']["id"]
    user, strings = get_user_data(chat_id)
    message_id = data.message["message_id"]
    if command == "reSendSMSCode":
        if is_flood(user, 60):
            # registration_resubmit(user.hive_id)
            pass
        else:
            now = datetime.datetime.now()
            if user.last_sms:
                time_left = now - user.last_sms
                edit_message_text(strings["re_send_message_err"].format(str(datetime.timedelta(seconds=60)-time_left)),
                                  chat_id, message_id)
    elif command == 'sendPost':
        delete_message(user.telegram_id, message_id)
        threading.Thread(target=re_post, args=(user, get_all_users_id())).start()
    elif command == 'cancelPost':
        edit_message_text(user.telegram_id, strings["cancel_post"], message_id)
        update_stable_id(user.telegram_id, None)
        update_stable_key(user.telegram_id, None)
    elif command == 'tries':
        threading.Thread(target=get_order_count, args=(user, strings)).start()
    elif command == 'start':
        start(user, strings)

# reply_markup=resend_message_inline_kb(strings, user.hive_id))
