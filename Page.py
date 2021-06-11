import requests
from bs4 import BeautifulSoup
import json
import os


class Page:

    def __init__(self, url, output=False):
        """
        self.content    > Content of the current page.
        self.url        > URL of the current page.
        self.next       > URL of the next page linked to the current page.
        self.title      > Title of the web novel.
        self.name       > Chapter number and name for the current page. 
        """
        self.output = output
        self.content = []
        self.url = url
        self.next = ''
        self.title = ''
        self.name = ''
        self.nextName = ''
        self.get_chapter()

    def get_chapter(self):
        """
        Grabs the page content from novelfull.com to be processed
        """
        response = requests.get(self.url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            self.process_response(soup)
        else:
            print("Error: {}".format(response.status_code))

    def process_response(self, soup):
        """
        Process the response to extract the relevant information.
        -page content
        -title
        -next chapter url
        """

        # Set next chapter url
        link = soup.find_all(
            "a", {"id": "next_chap"})[0].get('href')
        if link:
            self.next = "{}{}".format(self.url[:21], link)
            self.nextName = link.split('/')[-1].replace('.html', '')
        else:
            self.next = None
        # Set page content
        cutPoint = "© Copyright NovelFull.Com. All Rights Reserved."
        results = soup.find_all('p')
        self.content = []
        for i in range(len(results)):
            if cutPoint in results[i].text:
                break
            self.content.append(results[i].text)

        # set title and page name
        self.set_novel_info()

    def save_page_content(self):
        """
        Stores the page content for the current page URL.
        """
        path = os.path.join(os.getcwd(), 'novels', self.title)
        try:
            os.makedirs(path)
        except OSError:
            if self.output:
                print("{}Folder already exists".format(">" * 5))
        filename = os.path.join(path, "{}.json".format(self.name))
        content = self.get_data_as_dict()
        with open(filename, 'w', encoding="utf-8") as file:
            json.dump(content, file)
        print("{}\nStored: {}\n{}".format(
            "<>" * len(self.name), self.name, "<>" * len(self.name)))

    def set_novel_info(self):
        """
        Breaks down the url to extract the title of the novel
        and the name of the chapter.
        """
        parts = []
        for name in self.url.split('.'):
            parts.extend(name.split('/'))
        self.title = parts[4]
        self.name = parts[5]
        self.save_page_content()

    def get_next(self):
        return self.next

    def get_data_as_dict(self):
        d = {}
        d[self.name] = {
            'title': self.title,
            'name': self.name,
            'nextName': self.nextName,
            'url': self.url,
            'next': self.next,
            'content': self.content
        }
        return d

    def __str__(self):
        text = " URL:\t\t{}\n".format(self.url)
        text += " Novel Title:\t{}\n".format(self.title)
        text += " Chapter Name:\t{}\n".format(self.name)
        text += " Next Page URL:\t{}\n".format(self.next)
        return text


# Class Test
if __name__ == "__main__":
    print("\n Testing Class...\n")
    url = "https://novelfull.com/library-of-heavens-path/chapter-1-swindler.html"
    print(" Using the following url as the chapter of a novel.\n\n {}{}\n".format(
        ">"*5, url))

    print(" {}{} {}".format("*" * 100, "\n", "*" * 100))

    a = Page(url)
    print(a)
