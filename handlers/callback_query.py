from methods.unique import get_user_data
from methods.unique import is_flood, get_order_count
import threading
from handlers.command import start


async def callback_query_handler(client, callback_data):
    try:
        command, params = str(callback_data.data).split('_')
    except ValueError:
        command = callback_data.data
    user_id = callback_data.from_user.id
    user, strings = get_user_data(user_id)
    if is_flood(user, 3):
        if command == 'get':
            threading.Thread(target=get_order_count, args=(client, user, strings)).start()
    elif command == 'start':
        await start(client, user, strings)

# reply_markup=resend_message_inline_kb(strings, user.hive_id))
