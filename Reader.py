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
        self.index = 0
        self.last = 0

    def read_page(self):
        self.get_page()
        self.start_engine()

    def get_page(self):
        with open(self.lastPath, 'r', encoding='utf-8') as file:
            title = file.readline().strip('\n')
            name = file.readline().strip('\n')
            self.index = int(file.readline().strip('\n'))
            filename = os.path.join(
                os.getcwd(), 'novels', title, "{}.json".format(name))
            with open(filename, 'r') as obj:
                self.page = list(json.load(obj).values())[0]
        self.start_engine()

    def start_engine(self):
        engine = pyttsx3.init()
        engine.setProperty('rate', self.rate)
        engine.setProperty('volume', self.volume)
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[self.voice].id)
        self.last = len(self.page['content']) - 1
        line = []
        for i in range(self.index, len(self.page['content'])):
            self.store_next(i)
            line.append(self.page['content'][i])
        filename = "{}.mp3".format(self.page['name'])
        engine.save_to_file("".join(line), filename)
        print("Saving: {}".format(filename))
        engine.runAndWait()

    def store_next(self, i):
        with open(self.lastPath, 'w') as f:
            if i == self.last:
                f.write("{}\n".format(self.page['title']))
                f.write("{}\n".format(self.page['nextName']))
                f.write(str(0))
            else:
                f.write("{}\n".format(self.page['title']))
                f.write("{}\n".format(self.page['name']))
                f.write(str(i))
        if self.page['nextName']:
            pass
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
        except ValueError:
            print("Please enter a valid number.")
            self.set_rate()
        if rate <= 0:
            print("Please enter a value greater than 0")
            self.set_rate()
        else:
            self.rate = rate


if __name__ == "__main__":
    a = Reader(title='test-novel')
    a.read_page()
