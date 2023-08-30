import pyautogui as pag
import time
from random_word import RandomWords
from helpers import typeString, findImageTimeout
r = RandomWords()

# assuming phone stuck to bottom left manually

randomWords = [r.get_random_word() for i in range(int(input("How many words? ")))]
pag.PAUSE = 0

WAIT_TIME = 5

# url bar
pag.click(x=284, y=161)

# randomWords = ['hello', 'world', 'this', 'is', 'a', 'test'] * 10
# make list of 10 random words
# get number from user
print(randomWords)

tStart = time.time()

for word in randomWords:

    # get random word from list
    typeString(f"{word}\n")

    t1 = time.time()

    # wait for page to load
    # time.sleep(WAIT_TIME)

    findImageTimeout('searchMobile.jpg', 10)

    # calculate time taken for this word
    t2 = time.time()

    print(f"Time taken: {t2 - t1}s")

    # time taken * len(randomWords) - time taken for this word
    eta = (t2 - t1) * len(randomWords)

    # print eta
    print(f"ETA: {eta}s")

    # click x=284, y=161
    pag.click(x=284, y=161)
