
import os
import logging
from logging.handlers import RotatingFileHandler
from dotenv import load_dotenv
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton




#Bot token @Botfather, --⚠️ REQUIRED--
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7406407460:AAHvYL7lXKqh-PuHojT7SPicItACcfIajMo")

#Your API ID from my.telegram.org, --⚠️ REQUIRED--
APP_ID = int(os.environ.get("APP_ID", "20718334"))

#Your API Hash from my.telegram.org, --⚠️ REQUIRED--
API_HASH = os.environ.get("API_HASH", "4e81464b29d79c58d0ad8a0c55ece4a5")

#Your db channel Id --⚠️ REQUIRED--
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002177334941"))

#OWNER ID --⚠️ REQUIRED--
OWNER_ID = int(os.environ.get("OWNER_ID", "5585016974"))

#SUPPORT_GROUP: This is used for normal users for getting help if they don't understand how to use the bot --⚠ OPTIONAL--
SUPPORT_GROUP = os.environ.get("SUPPORT_GROUP", "-1002020461301")

#Port
PORT = os.environ.get("PORT", "8080")

#Database --⚠️ REQUIRED--
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://Umaid:umaid@cluster0.k2yxsvu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#Collection of pics for Bot // #Optional but atleast one pic link should be replaced if you don't want predefined links
PICS = (os.environ.get("PICS", "https://envs.sh/W9M.jpg https://envs.sh/3PQ.jpg https://envs.sh/Chb.jpg https://envs.sh/Ckc.jpg https://envs.sh/7nm.jpg")).split() #Required

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<blockquote expandable>{filename}</blockquote></b>")



START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/ec17880d61180d3312d6a.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://telegra.ph/file/e292b12890b8b4b9dcbd1.jpg")

QR_PIC = os.environ.get("QR_PIC", "https://envs.sh/B7w.png")



#==========================(BUY PREMIUM)====================#

PREMIUM_BUTTON = reply_markup=InlineKeyboardMarkup(
        [[InlineKeyboardButton("Remove Ads In One Click", callback_data="buy_prem")]]
)

PREMIUM_BUTTON2 = reply_markup=InlineKeyboardMarkup(
        [[InlineKeyboardButton("Remove Ads In One Click", callback_data="buy_prem")]]
) 

OWNER_TAG = os.environ.get("OWNER_TAG", "rohit_1888")

#UPI ID
UPI_ID = os.environ.get("UPI_ID", "rohit23pnb@axl")

#UPI QR CODE IMAGE
UPI_IMAGE_URL = os.environ.get("UPI_IMAGE_URL", "https://t.me/paymentbot6/2")

#SCREENSHOT URL of ADMIN for verification of payments
SCREENSHOT_URL = os.environ.get("SCREENSHOT_URL", f"t.me/rohit_1888")



#Time and its price

#7 Days
PRICE1 = os.environ.get("PRICE1", "0 rs")

#1 Month
PRICE2 = os.environ.get("PRICE2", "60 rs")

#3 Month
PRICE3 = os.environ.get("PRICE3", "150 rs")

#6 Month
PRICE4 = os.environ.get("PRICE4", "280 rs")

#1 Year
PRICE5 = os.environ.get("PRICE5", "550 rs")


#===================(END)========================#


#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("True", True) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Sharing Bot!"



LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
