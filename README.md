# WebReader

A simple command-line application for reading plain text files. The reader
splits files into pages, remembers your last read position for each book and
supports configurable page sizes.

## Key Features

- Remembers the last page read for multiple files
- Configurable number of lines per page
- Jump to a specific page or reset your progress
- Loads optional defaults from a `.env` file

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python main.py --file path/to/book.txt
```

### Options

- `--goto <page>` – start from a specific page (0 indexed)
- `--reset` – reset stored progress for the file
- `--page-size <lines>` – override number of lines per page

The application stores progress in `last_read.json`. Each entry maps a file
path to the next page that should be displayed.

### Example

```bash
python main.py --file book.txt --page-size 20
```

## How it Works

After each page is displayed, the reader saves the next page number to
`last_read.json`. When you restart the program with the same file it resumes
from where you left off.

## Limitations

- Only plain text files are supported.
- Page numbers are zero based when using `--goto`.
- `last_read.json` may grow if many unique file paths are used.

## Configuration

Copy `.env.example` to `.env` and adjust values:

```env
PAGE_SIZE=25
STATE_FILE=last_read.json
```

## Testing

Run the unit tests with:

```bash
pytest
```
