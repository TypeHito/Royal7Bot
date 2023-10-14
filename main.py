from core.api import app
from database.init_db import db
from methods.telegram_bot.bot_configs import reset_hook
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)


def main():
    reset_hook()
    db.connect()
    app.run()



if __name__ == "__main__":
    # os.system("start d:/NoneType/Install/ngrok http --domain=complete-curious-ram.ngrok-free.app 5000")
    while True:
        try:
            main()
        except Exception as err:
            print(err)

# start d:\NoneType\Install\ngrok http --domain=complete-curious-ram.ngrok-free.app 5000

