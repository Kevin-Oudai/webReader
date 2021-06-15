import pyttsx3
import json
import os


class Reader:

    def __init__(self, title, page=None, rate=250, volume=1.0, voice=1):
        """
        self.rate       > Set the words per minute speech rate.
                          Minimum rate should be 125 words per minute
                          but can be lower or higher.
        """
        self.rate = rate
        self.volume = volume
        self.voice = voice
        self.page = page
        self.title = title
        self.lastPath = os.path.join(
            os.getcwd(), 'novels', self.title, 'lastRead.txt')

    def read_page(self):
        self.get_page()
        self.start_engine()
        self.store_next()

    def get_page(self):
        with open(self.lastPath, 'r', encoding='utf-8') as file:
            title = file.readline().strip('\n')
            name = file.readline().strip('\n')
            filename = os.path.join(
                os.getcwd(), 'novels', title, "{}.json".format(name))
            with open(filename, 'r') as obj:
                self.page = list(json.load(obj).values())[0]

    def start_engine(self):
        engine = pyttsx3.init()
        engine.setProperty('rate', self.rate)
        engine.setProperty('volume', self.volume)
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[self.voice].id)
        intro = self.page['name'].replace('-', " ")
        print(intro)
        engine.say(intro)
        for line in self.page['content']:
            print(line)
            engine.say(line)
            engine.runAndWait()
        engine.stop()

    def store_next(self):
        if self.page['nextName']:
            with open(self.lastPath, 'w') as f:
                f.write("{}\n".format(self.page['title']))
                f.write(self.page['nextName'])
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


if __name__ == "__main__":
    a = Reader(title='test-novel')
    a.read_page()
