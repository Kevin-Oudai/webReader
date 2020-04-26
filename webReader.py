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
    
url = "https://wuxianovels.org/rebirth-of-the-thief-who-roamed-the-world/{}"
for i in range(204, 206):
    print("Reading Chapter {}".format(i))
    data = get_chapter(url.format(i))
    read_chapter(data)