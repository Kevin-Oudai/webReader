import requests
from bs4 import BeautifulSoup

class Page:
    def __init__(self, url):
        self.url = url
        self.html = self._get_html()
        self.soup = BeautifulSoup(self.html, 'html.parser')
        self.title = self._get_title()
        self.name = self._get_name()
        self.content = self._get_content()
        self.next = self._get_next()

    def _get_html(self):
        try:
            page = requests.get(self.url)
            page.raise_for_status()
            return page.text
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while trying to get the html: {e}")

    def _get_title(self):
        title = self.soup.find("h1").text
        return title

    def _get_name(self):
        name = self.soup.find("h2").text
        return name

    def _get_content(self):
        content = self.soup.find("div", {"id": "content"}).text
        return content

    def _get_next(self):
        next_page = self.soup.find("a", {"class": "next_page"})
        if next_page:
            return next_page["href"]
        else:
            return None

    def get_next(self):
        return self.next

    def get_content(self):
        return self.content

    def get_name(self):
        return self.name

    def get_title(self):
        return self.title
