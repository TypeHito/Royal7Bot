from methods.telegram_bot.bot_answer import send_message, send_photo, send_document
from database.users import update_current_menu, get_all_users, update_stable_key, update_stable_id, get_all_users_id
from methods.create_excel import create_excel
from methods.send_post import update_post_photo, update_post_text
from methods.unique import send_all, send_me


def admin_handler(msg, user, strings):
    if msg.text == "/get_list":
        send_message(user.telegram_id, "text 5")
    elif msg.text == "send_me":
        # send_me()
        return
    elif msg.text == "send_all":
        # print(get_all_users_id())
        send_message(5754619101, "clear")
        # send_all()
    elif msg.text == "GetList":
        create_excel(user.telegram_id, get_all_users())
        send_document(user.telegram_id, f'files_excel/user_date_{user.telegram_id}.xlsx')
    elif msg.text == "/send_post":
        send_photo(user.telegram_id, strings["main_banner"], strings["gifts"])
        update_current_menu(user.telegram_id, "send_post")
    elif msg.text == "/create":
        send_message(user.telegram_id, strings["create_post"])
        update_current_menu(user.telegram_id, "create_post")
        update_stable_id(user.telegram_id, None)
        update_stable_key(user.telegram_id, None)

    elif user.current_menu == "create_post":
        if msg.photo:
            update_post_photo(msg, user, strings)
        elif msg.text:
            update_post_text(msg, user)
        update_current_menu(user.telegram_id, "update_post")

    elif user.current_menu == "update_post":
        if msg.text:
            update_post_text(msg, user)
        update_current_menu(user.telegram_id, "main_menu")
    elif user.current_menu == "send_text":
        if msg.text:
            update_stable_key(user.telegram_id, msg.text)
            update_current_menu(user.telegram_id, "main_menu")
            send_photo(user.telegram_id, user.stable_id, user.stable_key + strings["accept_post"])