import platform
from pyrogram import idle

from online.core.clients import bot, LOGS

def Start_Bot():
    try:
        bot.start()
    except Exception as e:
        LOGS.info(e)
    LOGS.info("➖➖➖➖➖➖➖➖➖➖➖➖")
    LOGS.info(f"Python Version: Version - {platform.python_version()}")
    LOGS.info("➖➖➖➖➖➖➖➖➖➖➖➖")
    idle()


if __name__ == "__main__":
    Start_Bot()
    print(" Good Bye ! ")
