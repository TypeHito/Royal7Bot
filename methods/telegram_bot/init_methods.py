def get_user_id(response):
    msg = response.get("message")
    callback = response.get("callback_query")
    if msg:
        return msg['from']['id']
    if callback:
        return callback['from']['id']

