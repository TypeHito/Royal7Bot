from src.const import valid_users
from pyrogram.errors import PeerIdInvalid


def send_current(client, count):
    if count % 1000 == 0:
        for i in valid_users:
            client.send_message(i, f"Sended message count: {count}")


def post_message(client, receivers, text):
    count = 0
    for receiver in receivers:
        try:
            client.send_message((receiver[0]), text)
        except PeerIdInvalid:
            pass
        count += 1
        send_current(client, count)


def post_photo(client, receivers, photo, text, keyboard):
    count = 0
    for receiver in receivers:
        try:
            client.send_photo((receiver[0]), photo, text, reply_markup=keyboard)
        except PeerIdInvalid:
            pass

        count += 1
        send_current(client, count)


def post_video(client, receivers, video, text, keyboard):
    count = 0
    for receiver in receivers:
        try:
            client.send_video((receiver[0]), video, text, reply_markup=keyboard)
        except PeerIdInvalid:
            pass
        count += 1
        send_current(client, count)


def send_post(client, receivers, message_type, text=None, media=None, keyboard=None):
    # for i in valid_users:
    #     client.send_message(i, f"start Posting! {len(receivers)}")
    if message_type == "message":
        post_message(client, receivers, text, keyboard)
    elif message_type == "photo":
        post_photo(client, receivers, media, text, keyboard)
    elif message_type == "video":
        post_video(client, receivers, media, text, keyboard)
    # for i in valid_users:
    #     client.send_message(i, "End Posting!")

