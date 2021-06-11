# Novel Full WebReader

This is a python reader for novels on [Novel Full](https://novelfull.com/).

## How to use

1. Download the project as a zip file and unzip it in the desired folder
2. Open a command prompt and navigate to the folder containing the project files.
3. Install the requirements by entering

```
pip install -r requirements.txt
```

4. Go to [Novel Full](https://novelfull.com/) and copy the url for the first chapter of a novel. e.g.

```
https://novelfull.com/library-of-heavens-path/chapter-1-swindler.html
```

5. In the command prompt type

```
python main.py
```

and press enter. This will bring up the main menu.

6. You will be presented with the following menu.

```
  1. Pull Chapters
  2. Read Chapters
  0. Exit
  Enter a choice:
```

7. Press 1 and press enter. This will prompt you for the URL you copied in step 4.
8. Hold Ctrl and press 'v' to paste the URL and press enter. This will start pulling the chapters and storing them locally.

9. When the chapters are pulled the menu seen in step 6 will show again. You can choose to exit or start reader.

## Notes

- You can modify the chapter you wish to start reading from manually by going into the novels folder and open the folder for the title you wish to read then open the corresponding JSON file. Copy the title and the nextName into the lastRead.txt file one per line.
- You can pause the reader by clicking anywhere in the command prompt.
- This is the cleaned version of the reader. If you have any suggestions for the reader open an issue and I will work on it
- I will not make a GUI for the application until I am satisfied how the program works with the console.
