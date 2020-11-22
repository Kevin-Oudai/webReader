import requests
from bs4 import BeautifulSoup
import pyttsx3


def get_chapter(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        results = soup.find_all('p')
        # nextChp = soup.find_all("a", {"class": "next_page"})[0].get('href') <- for listnovel.com
        nextChp = soup.find_all("a", {"id": "next_chap"})[0].get('href')
        # cutPoint = '© 2019 ListNovel All rights reserved' <- for listnovel.com
        cutPoint = "© Copyright NovelFull.Com. All Rights Reserved."
        data = []
        for i in range(len(results)):
            if cutPoint in results[i].text:
                break
            data.append(results[i].text)
        return [data, nextChp]
    elif response.status_code == 404:
        return [["Page Not Found"], "No New Chapter"]


def read_chapter(data):
    engine = pyttsx3.init()
    # Change the rate of the reader to 250 when you are not reading along
    engine.setProperty('rate', 275)
    engine.setProperty('volume', 1.5)
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
    while i < numOfChapters:
        chapter = "https://novelfull.com{}".format(getLastRead())

        result = get_chapter(chapter)
        sym = len(chapter) + 11
        print("\n")
        print("#" * sym)
        print(" Reading: {}".format(chapter))
        print("#" * sym)
        read_chapter(result[0])
        storeNextChapter(result[1])
        i += 1


main()
