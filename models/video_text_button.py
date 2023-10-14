from methods.telegram_bot.inline_keyboard import inline_keyboard_button, inline_keyboard_markup
from methods.telegram_bot.bot_answer import send_video


def join_button():
    kb = inline_keyboard_markup()
    kb["inline_keyboard"].append([inline_keyboard_button("🗝 Imkoniyatlarni tekshirish", "tries")])
    kb["inline_keyboard"].append([inline_keyboard_button("🔄 Botni yangilash", "start")])
    return kb


def video_content_r7(user_id):
    text = """📞 1187 qisqa raqami orqali taksi chaqiring va 🎁 sovrinlardan birini qo"lga kiritish uchun imkoniyatlaringizni oshiring!

🎈 Shoshiling aksiya muddati tugashiga oz qoldi"""
    video = "BAACAgIAAxkBAAEHNDtlFbrizNJHmBmSVd77W8yrAAG5H_0AAr0zAAJb87FIPJk59z022kowBA"
    return send_video(user_id, video, text, reply_markup=join_button())


