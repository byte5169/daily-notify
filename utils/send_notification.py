import os
import requests
from datetime import datetime
from dotenv import load_dotenv
from utils.weather import get_weather
from utils.exchange_rates import get_exchange_rates
from config import COORDINATES_LON, COORDINATES_LAT

load_dotenv()
bot_token = os.getenv("BOT_TOKEN")
chat_id = os.getenv("CHAT_ID")


def message():
    """
    It returns a string with the current date and time, the current weather in Minsk, and the current
    exchange rates
    :return: A string.
    """
    msg = (
        f"""Today is {datetime.today().strftime("%d-%m-%Y")}.\n"""
        f"""{get_weather(COORDINATES_LAT, COORDINATES_LON)}\n"""
        f"""{get_exchange_rates(url="https://www.nbrb.by/")}\n"""
    )

    return msg


def send_message(msg=message()):
    """
    It sends a message to telegram

    :param msg: The message you want to send
    """
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={msg}"
    requests.get(url)


send_message()
