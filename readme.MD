# browser-bot

Simple browser automation script using **PyAutoGUI**.

This project demonstrates how to control the mouse and keyboard to
automate repetitive browser tasks. Example use case: sending contact
requests on ImmobilienScout24.

------------------------------------------------------------------------

## Requirements

-   Python 3.14+
-   Google Chrome
-   macOS (currently tested on macOS)
-   PyAutoGUI

Install dependencies:

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

## Environment Variables

Create a `.env` file in the project root:

``` bash
touch .env
```

Fill it with your credentials and personal data:

``` env
IMMOSCOUT_EMAIL=
IMMOSCOUT_PASSWORD=
NAME=
SURNAME=
PHONE=
STREET=
HOUSENUMBER=
ZIP=
CITY=
```
------------------------------------------------------------------------

## Usage

1.  Make sure your screen resolution and browser zoom match the expected
    layout. It was configured for the standard resolution for the macbook air M4: 1470 x 956 px
2.  Adjust coordinates and delays in the script if necessary.
(You can run the script at helpers/get_position.py, to get the position of where the mouse cursor is after 5 seconds, printed on the terminal/console)
3.  Run:

``` bash
python3 main.py
```

The script will: - Open Chrome - Navigate to ImmobilienScout24 - Log in
using `.env` credentials - Fill contact forms automatically

------------------------------------------------------------------------

## Notes

-   Automation depends on screen resolution and UI layout.
-   Add `time.sleep()` where necessary to improve stability.
-   Move the mouse to the top-left corner to trigger PyAutoGUI failsafe
    and stop execution.

------------------------------------------------------------------------

## Disclaimer

This project is for educational purposes only. Ensure compliance with
the website's Terms of Service before automating interactions.
