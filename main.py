from Page import Page
from Reader import Reader


def pull():
    url = str(input("Enter the url for the first page of the reader: "))
    firstPage = Page(url)
    page = firstPage
    while page.get_next():
        if page.get_next():
            page = Page(page.get_next())
        else:
            print("End of chapters")

    with open("lastRead.txt", 'w') as info:
        info.write("{}\n".format(firstPage.title))
        info.write(firstPage.name)


def read():
    numOfChapters = int(input("How many chapters do you want me to read?"))
    reader = Reader()
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
