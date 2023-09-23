import argparse
import time

import pyautogui as pag

from helpers import findCenterInArea, findImageTimeout, read_random_lines, typeInUrlBar

NUM_WORDS = 30
WORDS_FILE_PATH = "/Users/ssarfaraz/coding/personal/edgeRewards/words.txt"
pag.PAUSE = 0
WAIT_TIME = 1
# for notched mac
URL_X, URL_Y = 300, 55
# for regular pc
# urlX, urlY = 300, 30


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
    NUM_WORDS = args.numWords

randomWordsList = read_random_lines(WORDS_FILE_PATH, NUM_WORDS * 2)

# first half for desktop, second half for mobile
randomWordsDesktop = randomWordsList[:NUM_WORDS]
randomWordsMobile = randomWordsList[NUM_WORDS:]

t1 = time.time()
typeInUrlBar(randomWordsDesktop)
t2 = time.time()
print(f"Total time for desktop: {t2 - t1}")

# activate phone window
pag.hotkey("command", "option", "i")

t1 = time.time()
typeInUrlBar(randomWordsMobile)
t2 = time.time()
print(f"Total time for mobile: {t2 - t1}")

# close current tab
pag.hotkey("command", "w")

# new tab
pag.hotkey("command", "t")

# select url bar
pag.click(x=URL_X, y=URL_Y)

# go to https://rewards.bing.com/
pag.write("https://rewards.bing.com/")
pag.press("enter")
