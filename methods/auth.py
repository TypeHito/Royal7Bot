from src.const import valid_users


def is_login(user):
    if user.phone_number:
        return True
    return False


def is_valid_user(user):
    if user.telegram_id in valid_users:
        return True
    return False