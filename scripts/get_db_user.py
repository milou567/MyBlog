import os
from urllib.parse import urlsplit


def get_setting(setting_name, default=None, *, convert=lambda _value: _value or None):
    value = os.getenv(setting_name)
    if not value:
        try:
            from dynaconf import settings

            value = settings.get(setting_name)
        except ImportError:
            pass

    value = value or default
    return convert(value)


def get_db_username():
    url = get_setting("DATABASE_URL")
    if not url:
        return "--- no database configured ---"

    url = urlsplit(url)
    return url.username


def main():
    name = get_db_username()
    print(name)


if __name__ == "__main__":
    main()
