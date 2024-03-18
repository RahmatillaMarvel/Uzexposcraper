# UzexpoScraper

UzexpoScraper is a web scraper built with Scrapy for extracting news articles from [Uzbekistan Expo Centre](https://www.uzexpocentre.uz/) website in different languages (Uzbek, English, Russian, etc.) and saving the extracted data into a JSON file.

## Features

- Extracts news articles from [Uzbekistan Expo Centre](https://www.uzexpocentre.uz/) website.
- Supports multiple writing systems including Latin, Cyrillic, and English.
- Saves extracted data including URL, title, content, creation date, and access date into a JSON file.
- Pagination handling to scrape multiple pages of news articles.

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/RahmatillaMarvel/Uzexposcraper.git
    ```

2. Install dependencies:

    ```bash
    cd Uzexposcraper
    pip install -r requirements.txt
    ```

## Usage

To run the scraper, execute the following command:

```bash
scrapy crawl uzexpo_spider -a ws=<writing_system>
```

Replace `<writing_system>` with the desired writing system code (`lat` for Latin, `krill` for Cyrillic, `eng` for English, `rus` for Russian).

The scraped data will be saved in the `web/<name>/<writing_system>/uzexpo.json` file.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.