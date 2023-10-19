from database.users import update_stable_id, update_stable_key, update_current_menu
from methods.unique import get_user_data
import threading


def update_post_photo(msg, user, strings):
    last_photo = msg.photo[-1]
    photo_id = last_photo["file_id"]
    update_stable_id(user.telegram_id, photo_id)
    update_current_menu(user.telegram_id, "send_text")
    # send_photo(user.telegram_id, photo_id, strings["send_text"], reply_markup=ok_cancel(strings, "sendPost", "cancelPost"))


def update_post_text(msg, user):
    update_stable_key(user.telegram_id, msg.text)
    update_current_menu(user.telegram_id, "main_menu")
    user, strings = get_user_data(user.telegram_id)
    # if user.stable_id:
    #     send_photo(user.telegram_id, user.stable_id, user.stable_key + strings["accept_post"],
    #                reply_markup=ok_cancel(strings, "sendPost", "cancelPost"))
    #     return
    # send_message(user.telegram_id, user.stable_key + strings["accept_post"],
    #              reply_markup=ok_cancel(strings, "sendPost", "cancelPost"))


def send_post(user, receiver_id):
    pass
    # if user.stable_id:
    #     if user.stable_key:
    #         send_photo(receiver_id, user.stable_id, user.stable_key)
        # else:
        #     send_photo(receiver_id, user.stable_id)
    # else:
    #     send_message(receiver_id, user.stable_key)

        
def re_post(user, receivers):
    count = 0
    send_message(user.telegram_id, "Start\n sendMessageCount: " + str(len(receivers)))
    for chat_id in receivers:
        threading.Thread(target=send_post, args=(user, chat_id[0])).start()
        count += 1
        if count % 10 == 0:
            send_message(user.telegram_id, count)
