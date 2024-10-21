# PageWeaver

![Python](https://img.shields.io/badge/python-v3.9+-blue.svg)
![PyPI](https://img.shields.io/pypi/v/pageweaver.svg)
![License](https://img.shields.io/github/license/KTS-o7/pageweaver.svg)
![ViewCount](https://views.whatilearened.today/views/github/KTS-o7/pageweaver.svg)

This project is a CLI tool designed to crawl web novels from FreeWebNovel and generate a PDF document containing the chapters. The tool uses Python libraries such as `requests`, `BeautifulSoup`, and `pylatex` to fetch, process, and compile the novel content into a well-formatted PDF.

## Features

- Fetches novel chapters from FreeWebNovel.
- Processes and cleans the text to remove non-UTF8 characters.
- Generates a PDF document with a title page, table of contents, and chapters.
- Supports multi-threaded crawling for faster processing.
- Option to allow non-English characters in the novel title and author name.

## Requirements

- Python 3.9+
- `requests`
- `beautifulsoup4`
- `pylatex`
- `argparse`

## Installation

### Via pip

```bash
pip install pageweaver
```

### Via source

```bash
git clone https://github.com/KTS-o7/pageweaver.git
cd pageweaver
pip install -r requirements.txt
python setup.py install
```

## Usage

```bash
pageweaver <novel_url> <start_chapter_number> <end_chapter_number> [--output_dir <output_dir>] [--num-workers <num_workers>] [--allow-non-english]
```

### Arguments

- `novel_url`: The FreeWebNovel URL of the novel to crawl.
- `start_chapter`: The starting chapter number.
- `end_chapter`: The ending chapter number.
- `--output_dir`: (Optional) The destination directory for the generated PDF. Defaults to the current working directory.
- `--num-workers`: (Optional) The number of workers to use for crawling. Defaults to 10.
- `--allow-non-english`: (Optional) Allow non-English characters in the novel title and author name.

### Example Usage

```bash
pageweaver https://freewebnovel.com/global-fog-survival.html 1 15 --num-workers 5
pageweaver https://freewebnovel.com/global-fog-survival.html 1 30 --output_dir /path/to/output --allow-non-english
```

## How It Works

- **WebCrawler**: Fetches the HTML content of the novel chapters and extracts the text.
- **TextProcessor**: Cleans the text by removing non-UTF8 characters and escaping LaTeX special characters.
- **DocumentGenerator**: Uses pylatex to create a PDF document with the novel content.
- **NovelCrawlerService**: Manages the crawling process, coordinates the fetching and processing of chapters, and generates the final PDF.

### Example

To crawl the novel "Global Fog Survival" from chapters 1 to 2 and generate a PDF, run:

```bash
pageweaver https://freewebnovel.com/global-fog-survival.html 1 2 --num-workers 10
```

This will create a PDF document in the current working directory with the title and author extracted from the novel's metadata.

## License

This project is licensed under the MIT License.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Contact

For any questions or support, please open an issue on the GitHub repository.

## Disclaimer

This tool is not intended to promote piracy. It should be used for educational or personal reading purposes only. Please respect the copyrights of the original authors and publishers.

## Authors

- [Krishnatejaswi S](https://github.com/KTS-o7/)
- [Sridhar D Kedlaya](https://github.com/DeathStroke19891)

# Star Graph

![Star History Chart](https://api.star-history.com/svg?repos=KTS-o7/pageweaver&type=Date)
