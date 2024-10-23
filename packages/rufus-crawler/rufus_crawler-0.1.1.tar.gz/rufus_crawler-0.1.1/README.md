Rufus Crawler
=============

Rufus Crawler is a Python-based web crawling and content filtering tool designed to scrape web pages, extract relevant content, and refine the data using OpenAI's GPT models. It works on dynamic web pages rendered with JavaScript using Selenium, and it allows for recursive crawling with adjustable depth limits. The resulting data is then filtered based on user-defined instructions and saved in JSON format.

Features
--------

*   **Dynamic web page crawling**: Supports JavaScript-rendered web pages using Selenium.
*   **Depth-controlled crawling**: Crawl pages up to a user-defined depth, staying within the base domain.
*   **Content extraction**: Extracts text content from web pages and saves them in `.txt` files.
*   **Filtered content**: Uses OpenAI's GPT models to filter and refine the content based on user-provided instructions.
*   **Output in JSON format**: Final filtered content is saved in a `filtered_data.json` file.

Installation
------------

You can install the package directly from PyPI:

```bash
pip install rufus_crawler
```

Example Usage
-------------

```python
from rufus import RufusClient, ContentFilter

openai_api_key = "your_openai_api_key"
url = "https://example.com"
instructions = "Find information about product features and customer FAQs."

client = RufusClient(openai_api_key)
client.crawl(url, depth=2)
crawled_data = client.convert_txt_to_json()

content_filter = ContentFilter(openai_api_key)
filtered_data = content_filter.filter_content(instructions, crawled_data)
content_filter.save_filtered_data(filtered_data)
```

Project Structure
-----------------

```bash
rufus_crawler/
├── rufus/
│   ├── client.py            # Main RufusClient class
│   ├── content_filter.py    # ContentFilter class
│   ├── config.py            # Configuration settings
│   ├── utils.py             # Utility functions
├── scripts/
│   ├── run_rufus.py         # Main script to run the crawler
├── crawled_data/            # Directory to store intermediate crawled data
├── filtered_data.json       # Final output after filtering
├── requirements.yaml        # Conda environment dependencies
├── setup.py                 # Project setup for pip installation
└── README.md                # Project documentation (this file)
```

Setting up the Environment
--------------------------

Use the provided `requirements.yaml` file to set up a Conda environment:

1.  **Clone the repository**:

```bash
git clone https://github.com/yourusername/rufus_crawler.git
cd rufus_crawler
```

2.  **Install Conda** if you haven't already, and then create a new environment:

```bash
conda env create -f requirements.yaml
conda activate rufus-crawler
```

3.  **Install the Rufus Crawler package** in editable mode for development:

```bash
pip install -e .
```

Usage
-----

To configure the Rufus Crawler, you will need an OpenAI API key:

1.  **OpenAI API Key**: Obtain an API key from [OpenAI](https://platform.openai.com/signup/) if you don't have one.
2.  Edit the `run_rufus.py` script or your custom Python file to add your OpenAI API key, target URL, and instructions.

```python
openai_api_key = "your_openai_api_key"  # Replace with your OpenAI API key
url = "https://www.uta.edu/admissions/apply/graduate"
instructions = "We're making a chatbot for graduate admission process for UTA"
```

3.  Run the crawler:

```bash
python scripts/run_rufus.py
```

Workflow
--------

### 1\. Crawling and Saving Content

*   The `RufusClient` crawls the target URL recursively (depth controlled).
*   The dynamic content rendered by JavaScript is fetched using Selenium.
*   Extracted content is saved into `.txt` files within the `crawled_data/` directory.

### 2\. Convert TXT Files to JSON

*   The text files are converted to a JSON file, `crawled_data.json`.

### 3\. Filtering Content

*   The `ContentFilter` uses OpenAI's GPT to refine and filter the crawled content based on the provided instructions.
*   The refined data is saved into `filtered_data.json`.

### 4\. Cleanup

*   After successful filtering, all intermediate `.txt` files and directories are deleted, leaving only `filtered_data.json`.

License
-------

This project is licensed under the MIT License.
