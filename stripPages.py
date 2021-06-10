import requests
from bs4 import BeautifulSoup
from slugify import slugify


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
        return [["Page Not Found"], "page not found"]


def save_data(data, name):
    print(name)
    store = "chapters/{}.txt".format(name)
    content = " ".join(data[0])
    with open(store, 'w', encoding="utf-8") as f:
        f.writelines(content)


def getLastRead():
    with open("lastRead.txt") as f:
        last = str(f.read())
    return last


def storeNextChapter(chapter):
    with open("lastRead.txt", 'w') as f:
        f.write(chapter)


def getString(link):
    return "https://novelfull.com{}".format(link)


def main():

    chapter = getString(getLastRead())
    name = 2907
    while True:
        result = get_chapter(chapter)
        sym = len(chapter) + 11
        print("\n")
        print("#" * sym)
        print(" Storing: {}".format(result[1]))
        save_data(result, name)
        name+=1
        print("#" * sym)
        if result[1]:
            chapter = getString(result[1])
            
        else:
            break


main()
