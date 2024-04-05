from apps.telegram_client.helpers.main_actions import TMainAction


class TelegramManager:
    _instances = {}

    @classmethod
    def get_instance(cls, phone):
        if phone not in cls._instances:
            cls._instances[phone] = cls._create_instance(phone)

        return cls._instances[phone]

    @classmethod
    def remove_instance(cls, phone):
        if phone in cls._instances:
            del cls._instances[phone]

    @classmethod
    def _create_instance(cls, phone):
        tg = TMainAction.login(phone)

        state = tg.login(blocking=False)

        return {
            "tg": tg,
            "state": state
        }
