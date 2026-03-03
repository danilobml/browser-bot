import pyautogui
from pyautogui import Point
import time
import pyperclip  # type: ignore


pyautogui.PAUSE = 0.7


def click_on(position: Point) -> None:
    pyautogui.moveTo(position)
    pyautogui.click(position)


def click_sequence(*positions: Point) -> None:
    for position in positions:
        click_on(position)
        time.sleep(0.5)


def write_text(text: str) -> None:
    pyperclip.copy(text)
    pyautogui.hotkey("command", "v")


def write_and_skip(text: str) -> None:
    write_text(text)
    pyautogui.press("tab")


def open_chrome_incognito() -> None:
    pyautogui.hotkey("command", "space")
    pyautogui.write("Google Chrome")
    pyautogui.press("enter")
    pyautogui.hotkey("command", "shift", "n")


def open_site(url: str) -> None:
    pyautogui.hotkey("command", "l")
    write_text(url)
    pyautogui.press("enter")
    time.sleep(3)


def login_standard(
    email_input_position: Point,
    email: str,
    password: str,
    submit_position: Point,
) -> None:
    click_on(email_input_position)
    write_text(email)
    pyautogui.press("tab")
    write_text(password)
    click_on(submit_position)
    time.sleep(5)


def login_email_first(
    email_input_position: Point,
    email: str,
    password_input_position: Point,
    password: str,
    submit_position: Point,
) -> None:
    click_on(email_input_position)
    write_text(email)
    click_on(password_input_position)
    write_text(password)
    click_on(submit_position)
    time.sleep(5)
