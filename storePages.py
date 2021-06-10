from Page import Page

url = "https://novelfull.com/goddess-medical-doctor/chapter-0-prologue.html"

novel = {}
page = Page(url, True)
while page.get_next():
    novel.update(page.get_data_as_dict())
    if page.get_next():
        page = Page(page.get_next(), True)
    else:
        print("End of chapters")

for key, value in novel:
    print("{} {}".format(key, value['url']))
