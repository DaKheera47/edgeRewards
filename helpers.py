import time
import time
import pyautogui as pag
import os
import pyscreeze
import PIL
import random
from main import NUM_WORDS, WAIT_TIME, URL_X, URL_Y

# https://stackoverflow.com/questions/76361049/how-to-fix-typeerror-not-supported-between-instances-of-str-and-int-wh
__PIL_TUPLE_VERSION = tuple(int(x) for x in PIL.__version__.split("."))
pyscreeze.PIL__version__ = __PIL_TUPLE_VERSION

CUR_PATH = os.path.dirname(os.path.realpath(__file__))
DEFAULT_TIMEOUT = 10


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def findImage(imageUrl: str, confidence: int):
    try:
        x, y = pag.locateCenterOnScreen(
            f"{CUR_PATH}/static/{imageUrl}", confidence=confidence
        )
        return (x, y)
    except TypeError:
        return (-1, -1)


def enterTextInput(x: int, y: int, text: str, message: str):
    pag.click(x=x, y=y)
    pag.write(text.replace(" ", ""))
    pag.press("enter")


def findImageTimeout(
    imageUrl: str, timeout: int = DEFAULT_TIMEOUT, confidence: int = 0.90
):
    t1 = time.time()

    while True:
        t2 = time.time()

        if t2 - t1 < timeout:
            try:
                x, y = pag.locateCenterOnScreen(
                    f"{imageUrl}", confidence=confidence, grayscale=True
                )
                print(f"Found image at {x}, {y} after {t2 - t1}s")
                return (x, y)

            except TypeError:
                pass
        else:
            return (-1, -1)


def findCenterInArea(
    toFind: str, regionCoords, timeout: int = DEFAULT_TIMEOUT, confidence: int = 0.90
):
    t1 = time.time()

    while True:
        t2 = time.time()

        if t2 - t1 < timeout:
            try:
                region = pag.screenshot(region=regionCoords)

                x, y = pag.center(
                    pag.locate(toFind, region, confidence=confidence, grayscale=True)
                )

                # print(f"Found image at {x}, {y} after {t2 - t1}s")
                return (x, y)

            except TypeError:
                pass
        else:
            return (-1, -1)


def read_random_lines(file_path, count):
    # Get total number of lines in the file
    with open(file_path, "r") as f:
        total_lines = sum(1 for _ in f)

    random_words = []

    with open(file_path, "r") as f:
        # Randomly pick starting line
        start_line = random.randint(0, total_lines - count)

        # Skip to the starting line
        for _ in range(start_line):
            next(f)

        # Read the desired number of lines
        for _ in range(count):
            random_words.append(f.readline().strip())

    return random_words


def printRandomWords(words):
    for idx, word in enumerate(words, start=1):
        print(f"{idx}. {word}")


def typeInUrlBar(words):
    # url bar
    pag.click(x=URL_X, y=URL_Y)

    for idx, word in enumerate(words):
        # get random word from list
        pag.write(f"[{idx + 1}/{NUM_WORDS}] - {word}")
        pag.press("enter")

        # wait to load page
        time.sleep(WAIT_TIME)

        # reset url bar
        pag.click(x=URL_X, y=URL_Y)
