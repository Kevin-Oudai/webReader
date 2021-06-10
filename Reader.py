import pyttsx3
from Page


class Reader:

    def __init__(self, rate=280, volume=1.0, voice=1):
        """
        self.rate       > Set the words per minute speech rate.
                          Minimum rate should be 125 words per minute
                          but can be lower or higher.
        """
        self.rate = rate
        self.volume = volume
        self.voice = voice
        self.page = None
        self.get_page()

    def get_page(self):
        with open("lastRead.txt", 'r', encoding='utf-8') as file:
            filename = "{}.json".format(file.read())
            with open(filename, 'r') as pageObject:
                self.page = json.load(pageObject)

    def read_page(self, data):
        engine = pyttsx3.init()
        engine.setProperty('rate', self.rate)
        engine.setProperty('volume', self.volume)
        engine.setProperty('voice', self.voice)
        engine.say(self.page.name.replace('-', " "))
        for line in self.page.content:
            print(line)
            engine.say(line)
            engine.runAndWait()
        engine.stop()
        self.store_last_read()

    def store_last_read(self):
        if self.page.next:
            with open("lastRead.txt", 'w') as f:
                f.write(self.page.next)
        else:
            print("This is the last stored chapter")

    def set_volume(self):
        volume = float(input("Enter a value from 0 to 1: "))
        if volume > 1 or volume < 0:
            print("Please enter a valid value.")
            self.set_volume()
        else:
            self.volume = volume

    def set_rate(self):
        try:
            rate = int(input("Enter words per minute reading rate: "))
        except BaseException as err:
            print("Message: {}".format(err.message))
            self.set_rate()
        if rate <= 0:
            print("Please enter a value greater than 0")
            self.set_rate()
        else:
            self.rate = rate


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
