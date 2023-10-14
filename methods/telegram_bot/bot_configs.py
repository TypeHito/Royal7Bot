# TOKEN = "6359664328:AAFsmvUHm3il2UtmO-0DpiEbYHH8Ee4RYHQ"
TOKEN = "6622255440:AAEkbsxerXozjxOppwRLGN4Yf2dvwW70-to"

URL = f"""https://api.telegram.org/bot{TOKEN}/"""
BOT_URL = "bot"
SERVER = "https://complete-curious-ram.ngrok-free.app/" + BOT_URL


def reset_hook():
    from methods.telegram_bot.bot_answer import send_message
    from core.const import valid_users
    del_web_hook = f"{URL}deleteWebhook"
    set_web_hook = f"{URL}setWebhook?url={SERVER}"
    send_message(valid_users[0],
                 "Reset bot Webhook\n"
                 f"[❌del webhook]({del_web_hook})\n"
                 f"[✅set webhook]({set_web_hook})\n"
                 f"server = {SERVER}")

