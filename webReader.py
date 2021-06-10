import requests
from bs4 import BeautifulSoup
import pyttsx3

def get_chapter(name):
    loc = "chapters/{}".format(name)
    with open(loc, 'r', encoding='utf-8') as file:
        return file.read().split(".")

def read_chapter(data):
    engine = pyttsx3.init()
    # Change the rate of the reader to 250 when you are not reading along
    engine.setProperty('rate', 280)
    engine.setProperty('volume', 3.0)
    for line in data:
        print(line)
        engine.say(line)
        engine.runAndWait()
    engine.stop()


def getLastRead():
    with open("lastRead.txt") as f:
        last = str(f.read())
    return last


def storeNextChapter(chapter):
    with open("lastRead.txt", 'w') as f:
        f.write(chapter)


def main():
    numOfChapters = int(input("How many chapters do you want to read? "))
    i = 0
    name = 2907
    while i < numOfChapters:
        chapter = "{}.txt".format(name)
        result = get_chapter(chapter)
        sym = len(chapter) + 11
        print("\n")
        print("#" * sym)
        print(" Reading: {}".format(chapter))
        print("#" * sym)
        read_chapter(result)
        name += 1


main()
