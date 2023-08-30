import argparse
import time

import pyautogui as pag
from random_word import RandomWords

from helpers import findCenterInArea, findImageTimeout

r = RandomWords()
numWords = 35

# check if something is defined in args
# if so, use that as numWords
# else, use default value
parser = argparse.ArgumentParser()
parser.add_argument(
    "-n",
    "--numWords",
    type=int,
    help="number of words to search for",
)
args = parser.parse_args()

if args.numWords:
    numWords = args.numWords

randomWordsList = [r.get_random_word() for i in range(numWords * 2)]

# first half for desktop, second half for mobile
randomWordsDesktop = randomWordsList[:numWords]
randomWordsMobile = randomWordsList[numWords:]

pag.PAUSE = 0.1
WAIT_TIME = 1

# for regular pc
# urlX, urlY = 300, 30

# for notched mac
urlX, urlY = 300, 55


def printRandomWords(words):
    for idx, word in enumerate(words, start=1):
        print(f"{idx}. {word}")


# give time to switch to browser
time.sleep(WAIT_TIME)

# click on url bar
pag.click(x=urlX, y=urlY)

t1 = time.time()
for idx, word in enumerate(randomWordsDesktop):
    # get random word from list
    pag.write(f"[{idx + 1}/{numWords}] - {word}")
    pag.press("enter")

    # try to find image, if found, continue
    # findImageTimeout("./name.jpg")
    findCenterInArea("./desktopSearch.jpg", regionCoords=(210, 157, 104, 53))

    # reset url bar
    pag.click(x=urlX, y=urlY)

t2 = time.time()
print(f"Total time for desktop: {t2 - t1}")

# activate phone window
pag.hotkey("command", "option", "i")

# url bar
pag.click(x=urlX, y=urlY)

t1 = time.time()
for idx, word in enumerate(randomWordsMobile):
    # get random word from list
    pag.write(f"[{idx + 1}/{numWords}] - {word}")
    pag.press("enter")

    # try to find image, if found, continue
    findCenterInArea("./mobileMic.jpg", regionCoords=(576, 208, 50, 65))
    # findImageTimeout("./mobileMic.jpg")

    # reset url bar
    pag.click(x=urlX, y=urlY)

t2 = time.time()
print(f"Total time for mobile: {t2 - t1}")

# close current tab
pag.hotkey("command", "w")

# new tab
pag.hotkey("command", "t")

# select url bar
pag.click(x=urlX, y=urlY)

# go to https://rewards.bing.com/
pag.write("https://rewards.bing.com/")
pag.press("enter")
