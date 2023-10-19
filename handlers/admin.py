from database.users import update_current_menu, get_all_users, update_stable_key, update_stable_id
from methods.create_excel import create_excel
from methods.send_post import update_post_photo, update_post_text


async def admin_handler(client, message, user, strings):
    if message.text == "/get_list":
        client.send_message(user.telegram_id, "text 5")
    elif message.text == "send_me":
        # send_me()
        return
    elif message.text == "send_all":
        # print(get_all_users_id())
        client.send_message(5754619101, "clear")
        # send_all()
    elif message.text == "GetList":
        create_excel(user.telegram_id, get_all_users())
        client.send_document(user.telegram_id, f'files_excel/user_date_{user.telegram_id}.xlsx')
    elif message.text == "/send_post":
        client.send_photo(user.telegram_id, strings["main_banner"], strings["gifts"])
        update_current_menu(user.telegram_id, "send_post")
    elif message.text == "/create":
        client.send_message(user.telegram_id, strings["create_post"])
        update_current_menu(user.telegram_id, "create_post")
        update_stable_id(user.telegram_id, None)
        update_stable_key(user.telegram_id, None)

    elif user.current_menu == "create_post":
        if message.photo:
            update_post_photo(message, user, strings)
        elif message.text:
            update_post_text(message, user)
        update_current_menu(user.telegram_id, "update_post")

    elif user.current_menu == "update_post":
        if message.text:
            update_post_text(message, user)
        update_current_menu(user.telegram_id, "main_menu")
    elif user.current_menu == "send_text":
        if message.text:
            update_stable_key(user.telegram_id, message.text)
            update_current_menu(user.telegram_id, "main_menu")
            client.send_photo(user.telegram_id, user.stable_id, user.stable_key + strings["accept_post"])