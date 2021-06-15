# Novel Full WebReader

This is a python reader for novels on [Novel Full](https://novelfull.com/).

## Setup

### Download Zip

1. Download the project as a zip file and unzip it in the desired folder
2. Open a **command prompt** or **terminal** and navigate to the folder containing the project files.
3. Install the requirements by typing

```
pip install -r requirements.txt
```

in the **command prompt** or **terminal** then press enter.

```
https://novelfull.com/library-of-heavens-path/chapter-1-swindler.html
```

### Cloning the Source Code

1. Copy the git url for this repository

```
https://github.com/Kevin-Oudai/webReader.git
```

2. Open a **command prompt** or **terminal** and navigate to the folder in which you wish to save the source code.
3. Type

```
git clone https://github.com/Kevin-Oudai/webReader.git
```

and press enter.

2. When the files a finished copying install the requirements by typing

```
pip install -r requirements.txt
```

in the **command prompt** or **terminal** then press enter.

## How to Use

### Downloading a Title

1. Open a **command prompt** or **terminal** and navigate to the folder with the source code
2. Type

```
python main.py
```

and press enter. This will bring up the main menu. You will be presented with the following menu.

```
  1. Pull Chapters
  2. Read Chapters
  0. Exit
  Enter a choice:
```

3. If you are running the program for the first time press 1 and press enter.
4. Go to [Novel Full](https://novelfull.com/) and copy the url for the first chapter of a novel you wish to read. e.g.

```
https://novelfull.com/library-of-heavens-path/chapter-1-swindler.html
```

5. Hold Ctrl and press 'v' to paste the URL and press enter. This will start pulling the chapters and storing them locally.
6. After the chapters are finished pulling you can also pull chapters from other titles by repeating step 3 to 5 or start from step 1 if you closed the terminal.

### Reading a Title

1. Open a **command prompt** or **terminal** and navigate to the folder with the source code
2. Type

```
python main.py
```

and press enter. This will bring up the main menu. You will be presented with the following menu.

```
  1. Pull Chapters
  2. Read Chapters
  0. Exit
  Enter a choice:
```

3. Press 2 and then press enter.
4. You will be presented with a menu showing all the titles you downloaded.
5. Select a title by entering the corresponding number.
6. Enter the number of chapters you want read to you and press enter.

## Notes

- You can modify the chapter you wish to start reading from manually by going into the novels folder and open the folder for the title you wish to read then open the corresponding JSON file. Copy the title, the name and 0 (zero) into the lastRead.txt file one per line. Save the file and the start main.py and choose option 2.
- You can pause the reader by clicking anywhere in the command prompt.
- You can close the reader whenever you wish. When you continue reading that title again it will continue from the last line that was being read when you closed the program.
- This is the cleaned version of the reader. If you have any suggestions for the reader open an issue and I will work on it
- I will not make a GUI for the application until I am satisfied with the console version of the program.
