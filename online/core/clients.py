from pyrogram import Client
from online.Config import *
from pyromod import listen
import logging
from logging.handlers import RotatingFileHandler

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s [%(filename)s:%(lineno)d]",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler("Legend.txt", maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


LOGS = logging.getLogger("LEGEND")

bot = Client(
    "ironman",
    bot_token=bot_token,
    api_id=api_id,
    api_hash=api_hash,
    plugins=dict(root="online.plugins"),
)
