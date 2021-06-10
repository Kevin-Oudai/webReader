# Novel Full WebReader

This is a python reader for novels on (Novel Full)[https://novelfull.com/].

## How to use

1. Download the project as a zip file and unzip it in the desired folder
2. Open a command prompt and navigate to the folder containing the project files.
3. Install the requirements by entering

```
pip install -r requirements.txt
```

4. Go to (Novel Full)[https://novelfull.com/] and choose the first chapter of a novel. e.g. https://novelfull.com/library-of-heavens-path/chapter-1-swindler.html
5. Copy the text after '.com' into the file named lastRead.txt and save it.e.g. /library-of-heavens-path/chapter-1-swindler.html
6. In the command prompt type

```
python stripPages.py
```

and press enter. This will start striping the pages up to the most recent chapter. 7. Once the this is finished open the file named webReader.py and ensure the name variable is set to 1. 8. In the command prompt type

```
python webReader.py
```

and press enter. 9. Enter the amount of chapters you want read to you and press enter this will start the reader.

## Notes

- The name variable in webReader.py needs to be changed to the chapter number you wish to start from everytime you close the reader.
- You can pause the reader by clicking anywhere in the command prompt.
- This is the first version of the reader so it is not very user friendly as the project progressed this will be fixed.ew
