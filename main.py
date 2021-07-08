from Page import Page
from Reader import Reader
import os


def pull():
    url = str(input("Enter the url for the first page of the reader: "))
    firstPage = Page(url)
    page = firstPage
    while page.get_next():
        if page.get_next():
            page = Page(page.get_next())
        else:
            print("End of chapters")

    path = os.path.join(os.getcwd(), 'novels', firstPage.title, "lastRead.txt")
    with open(path, 'w', encoding='utf-8') as info:
        info.write("{}\n".format(firstPage.title))
        info.write("{}\n".format(firstPage.name))
        info.write(str(0))


def read():
    path = os.path.join(os.getcwd(), 'novels')
    novels = os.listdir(path)
    for index, novel in enumerate(novels):
        print("{}. {}".format(index + 1, novel))
    choice = int(input("Choose a title: "))
    title = novels[choice - 1]
    numOfChapters = int(input("How many chapters do you want me to read?"))
    reader = Reader(title)
    for i in range(numOfChapters):
        reader.read_page()


while True:
    print("  1. Pull Chapters")
    print("  2. Read Chapters")
    print("  0. Exit")
    choice = int(input("  Enter a choice: "))
    if choice == 1:
        pull()
    elif choice == 2:
        read()
    elif choice == 0:
        break
    else:
        print("   Error!!!")
        print("   Try again")
