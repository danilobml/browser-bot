import os
import pyautogui
from pyautogui import Point
import time
from dotenv import load_dotenv
from lib.bot_interface import click_on, write_text, write_and_skip

load_dotenv()


# Immoscout Site specific:
def search_apartment(
    city: str,
    num_bedrooms: int,
    max_price: int,
    max_distance_from_center: int,
) -> None:
    # Hardcoded for ImmoScout:
    city_position = Point(x=489, y=462)
    max_price_position = Point(x=403, y=511)
    select_num_bedrooms_position = Point(x=576, y=505)
    select_distance_position = Point(x=705, y=509)
    submit_position = Point(x=971, y=507)
    num_bedrooms_positions = {
        2: Point(x=551, y=636),
        3: Point(x=581, y=705),
    }
    distance_positions = {
        5: Point(x=699, y=702),
        10: Point(x=671, y=733),
        15: Point(x=677, y=753),
    }

    click_on(city_position)
    write_text(city)
    pyautogui.press("enter")
    click_on(max_price_position)
    write_text(str(max_price))
    if num_bedrooms:
        if num_bedrooms_position := num_bedrooms_positions.get(num_bedrooms):
            click_on(select_num_bedrooms_position)
            click_on(num_bedrooms_position)
    if max_distance_from_center:
        if distance_position := distance_positions.get(max_distance_from_center):
            click_on(select_distance_position)
            click_on(distance_position)
    click_on(submit_position)


def apply_to_apartment(result: int, message: str) -> None:
    # Hardcoded
    result_positions = {
        1: Point(x=182, y=560),
    }
    start_position = Point(x=889, y=738)
    message_position = Point(x=542, y=476)
    select_title_position = Point(x=597, y=687)
    title_position = Point(x=548, y=759)
    name_position = Point(x=521, y=773)
    select_persons_position = Point(x=608, y=582)
    persons_position = Point(x=584, y=629)
    select_pets_position = Point(x=549, y=649)
    pets_position = Point(x=550, y=697)
    select_job_position = Point(x=582, y=729)
    job_position = Point(x=555, y=757)
    select_income_position = Point(x=560, y=814)
    income_position = Point(x=541, y=774)
    select_documents_position = Point(x=617, y=470)
    documents_position = Point(x=598, y=434)
    submit_position = Point(x=701, y=785)

    if result_position := result_positions.get(result):
        click_on(result_position)
    else:
        return

    time.sleep(3)
    click_on(start_position)
    click_on(message_position)
    write_text(message)
    click_on(select_title_position)
    click_on(title_position)
    click_on(name_position)
    write_and_skip(os.getenv("NAME") or "")
    write_and_skip(os.getenv("SURNAME") or "")
    write_and_skip(os.getenv("PHONE") or "")
    write_and_skip(os.getenv("STREET") or "")
    write_and_skip(os.getenv("HOUSENUMBER") or "")
    write_and_skip(os.getenv("ZIP") or "")
    write_and_skip(os.getenv("CITY") or "")
    click_on(select_persons_position)
    click_on(persons_position)
    click_on(select_pets_position)
    click_on(pets_position)
    click_on(select_job_position)
    click_on(job_position)
    click_on(select_income_position)
    click_on(income_position)
    pyautogui.scroll(-100000)
    click_on(select_documents_position)
    click_on(documents_position)
    click_on(submit_position)
