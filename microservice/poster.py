from microservice.telegram_bot.bot_answer import send_message, send_photo
from src.const import last_post, last_post_text, valid_users, valid_users_res, gift_text, action_photo
from database.users import get_all_users_id
from microservice.telegram_bot.inline_keyboard import inline_keyboard_markup, inline_keyboard_button
import time
import json
from database.init_db import db


def buttons():
    kb = inline_keyboard_markup()
    kb['inline_keyboard'].append(
        [
            inline_keyboard_button( "🗝 Imkonyatlarni tekshirish", "get"),
            # inline_keyboard_button("🔄Botni yangilash", "start")
        ]
    )
    return kb


def send_me():
    # users = get_all_users_id()
    users = valid_users_res

    count = 0
    incorrect = {}

    for i in valid_users:
        send_message(i, f"start posting: {len(users)}")

    for user in users:
        try:
            msg = send_photo(user[0], last_post, last_post_text, reply_markup=buttons())
            if not msg['ok']:
                incorrect[user[0]] = str(msg)
        except Exception as err:
            incorrect[user[0]] = str(err)
        count += 1

        if count % 1000 == 0:
            send_message(valid_users[0], f"Post message count: {count}")
            time.sleep(1)

    with open("errors.json", "w") as f:
        json.dump(incorrect, f, indent=2)

    for i in valid_users:
        send_message(i, f"Posting End: \nPosted: {len(users)}\nCan'tPost count: {len(incorrect) }")


def send_one(user_id, gift_id):
    status = ""
    send = False
    try:
        if 1 <= gift_id <= 7:
            current = gift_id-1
            msg = send_photo(user_id, action_photo[current], gift_text[current], reply_markup=buttons())
            send = msg['ok']
            if not send:
                status = "Error:" + str(user_id) + ":" + str(msg)
            time.sleep(2)
            for i in valid_users:
                send_photo(i, action_photo[current],
                           str(f"user_id {user_id}:\n" + str(gift_text[current]) + f"\nsend status: {send}"),
                           reply_markup=buttons())
        else:
            status = "Error: Index gift_id out of range"

    except Exception as ex_err:
        status = "Error:" + str(user_id) + ":" + str(ex_err)

    print(status)
    for i in valid_users:
        send_message(i, status)


def send_all():
    users = get_all_users_id()
    # users = valid_users_res

    count = 0
    incorrect = {}

    for i in valid_users:
        send_message(i, f"start posting: {len(users)}")

    for user in users:
        try:
            msg = send_photo(user[0], last_post, last_post_text, reply_markup=buttons())

            if not msg['ok']:
                incorrect[user[0]] = str(msg)
                print("post", user[0], " ERROR!", count)
            else:
                print("post", user[0], " send!",  count)
        except Exception as err:
            incorrect[user[0]] = str(err)
        count += 1

        if count % 1000 == 0:
            send_message(valid_users[0], f"Post message count: {count}")
            time.sleep(1)

    with open("errors2.json", "w") as f:
        json.dump(incorrect, f, indent=2)

    for i in valid_users:
        send_message(i, f"Posting End: \nPosted: {len(users)}\nCan'tPost count: {len(incorrect)}")


# db.connect()
# send_me()
# send_all()
def main():
    user_id_input = int(input("telegram_id: "))
    count = 1
    for _ in gift_text:
        print(count, _)
        count += 1

    user_gift_input = int(input("gift_id: "))
    send_one(user_id_input, user_gift_input)


while True:
    try:
        main()
    except Exception as err:
        print(err)
