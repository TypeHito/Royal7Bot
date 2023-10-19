class User:
    def __init__(self, user_id, telegram_id, phone_number, order_count, gift_type, last_command, last_sms, current_menu,
                 lang, hive_id, stable_id, stable_key, create_at):
        self.user_id = user_id
        self.telegram_id = telegram_id
        self.phone_number = phone_number
        self.order_count = order_count
        self.gift_type = gift_type
        self.last_command = last_command
        self.last_sms = last_sms
        self.current_menu = current_menu
        self.language = lang

        self.hive_id = hive_id
        self.stable_id = stable_id
        self.stable_key = stable_key
        self.create_at = create_at

    def get_json(self):
        return {
            "user_id": self.user_id,
            "telegram_id": self.telegram_id,
            "phone_number": self.phone_number,
            "order_count": self.order_count,
            "gift_type": self.gift_type,
            "last_command": self.last_command,
            "last_sms": self.last_sms,
            "current_menu": self.current_menu,
            "language": self.language,
            "hive_id": self.hive_id,
            "stable_id": self.stable_id,
            "stable_key": self.stable_key,
            "create_at": self.create_at

        }

    def get_data(self):
        return (
            self.user_id,
            self.telegram_id,
            self.phone_number,
            self.order_count,
            self.gift_type,
            self.last_command,
            self.last_sms,
            self.current_menu,
            self.language,
            self.hive_id,
            self.stable_id,
            self.stable_key,
            self.create_at
        )

