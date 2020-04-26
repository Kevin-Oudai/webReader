import requests
from bs4 import BeautifulSoup
import pyttsx3

def get_chapter(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        cutPoint = "If you find any errors ( broken links, non-standard content, etc.. ),"
        results = soup.find_all('p')
        data = []
        for i in range(2, len(results)):
            if cutPoint in results[i].text:
                break
            data.append(results[i].text)
        return data
    elif response.status_code == 404:
        return ["Page Not Found"]

def read_chapter(data):
    engine = pyttsx3.init()
    # Change the rate of the reader to 250 when you are not reading along
    engine.setProperty('rate', 300)
    engine.setProperty('volume', 1.5)
    for line in data:
        engine.say(line)
        engine.runAndWait()
    engine.stop()

def getLastRead():
    with open("lastRead.txt") as f:
        last = f.read()
    return last

def storeLastRead(chapter):
    with open("lastRead.txt", 'w') as f:
        f.write(chapter)

def main():
    base = "https://wuxianovels.org/{}/{}"
    novel = "rebirth-of-the-thief-who-roamed-the-world"
    # Chapter needs to change when the program starts each time
    chapter = getLastRead()
    numOfChapters = input("How many chapters do you want to read? ")
    for i in range(chapter, chapter + numOfChapters):
        url = base.format(novel, i)
        print("Reading Chapter {}".format(i))
        data = get_chapter(url)
        read_chapter(data)
    storeLastRead(chapter + numOfChapters)
main()