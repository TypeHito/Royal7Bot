from methods.telegram_bot.reply_keyboard import reply_keyboard_markup, reply_keyboard_button


def main_manu(strings, is_admin=False, contact=False):
    kb = reply_keyboard_markup(True, False)
    kb['keyboard'].append([reply_keyboard_button(strings["main_menu_1"]), reply_keyboard_button(strings["main_menu_2"])])
    kb['keyboard'].append([reply_keyboard_button(strings["main_menu_3"])])
    # kb['keyboard'].append([reply_keyboard_button(strings["send_number"], request_contact=True)])
    if is_admin:
        kb['keyboard'].append([reply_keyboard_button("GetList")])
    return kb
