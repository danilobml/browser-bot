import os
from pyautogui import Point
import time
from dotenv import load_dotenv
from lib.bot_interface import (
    open_chrome_incognito,
    open_site,
    click_sequence,
    login_email_first
)
from immoscout.api import search_apartment, apply_to_apartment
from immoscout.get_message import get_message


load_dotenv()


def main():
    base_url = "immobilienscout24.de"
    search_url = "immobilienscout24.de/wohnen/mietwohnungen.html"
    email = os.getenv("IMMOSCOUT_EMAIL")
    password = os.getenv("IMMOSCOUT_PASSWORD")
    city = "Berlin"
    num_bedrooms = 2
    max_price = 1000
    max_distance_from_center = 10
    message = get_message("immoscout/generic_message.txt")

    # Go to site:
    open_chrome_incognito()
    open_site(base_url)
    time.sleep(2)

    # positions depend on monitor resolution (here standard for the macbook air M: 1470 x 956)
    confirm_cookies = Point(x=850, y=738)
    register = Point(x=1240, y=164)
    click_sequence(confirm_cookies, register)

    # login:
    email_input_position = Point(x=1005, y=678)
    confirm_email_position = Point(x=1126, y=622)
    confirm_password_position = Point(x=1139, y=487)
    login_email_first(
        email_input_position,
        email,
        confirm_email_position,
        password,
        confirm_password_position,
    )

    # search:
    open_site(search_url)
    search_apartment(city, num_bedrooms, max_price, max_distance_from_center)
    apply_to_apartment(1, message)


if __name__ == "__main__":
    main()
