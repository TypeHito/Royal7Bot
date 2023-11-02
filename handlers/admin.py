from database.users import update_current_menu, get_all_users, update_stable_key, update_stable_id, get_all_users_id
from methods.create_excel import create_excel
from methods.poster import send_post
from src import const
from models.buttons import menu_keyboards


async def admin_handler(client, message, user, strings):
    if message.text == "/get_list":
        create_excel(user.telegram_id, get_all_users())
        await client.send_document(user.telegram_id, f'files_excel/user_date_{user.telegram_id}.xlsx')
    elif message.text == "GetList":
        create_excel(user.telegram_id, get_all_users())
        await client.send_document(user.telegram_id, f'files_excel/user_date_{user.telegram_id}.xlsx')
    elif message.text == "/send_me":
        button = menu_keyboards.get_start("🗝 Imkonyatlarni tekshirish", "🔄Botni yangilash")

        await send_post(client, const.valid_users_res, "photo", const.last_post_text, const.last_post, button)
    elif message.text == "/send_all":
        button = menu_keyboards.get_start("🗝 Imkonyatlarni tekshirish", "🔄Botni yangilash")
        await send_post(client, get_all_users_id(), "photo", const.last_post_text, const.last_post, button)
