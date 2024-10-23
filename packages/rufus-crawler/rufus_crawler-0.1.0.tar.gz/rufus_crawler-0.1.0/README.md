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

Requirements
------------

To install the dependencies for this project, use the provided `requirements.yaml` file for setting up a `conda` environment.

### Install the Dependencies

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/rufus_crawler.git
    cd rufus_crawler
    ```

2.  **Install Conda** if you haven't already, then create a new environment using `requirements.yaml`:
    
    ```bash
    conda env create -f requirements.yaml
    conda activate rufus-crawler
    ```
    
2.  **Install the Rufus Crawler package** in editable mode for development:
    
    ```bash
    pip install -e .
    ```
    

### Project Structure

```python
rufus_crawler/
├── rufus/
│   ├── client.py             # Main RufusClient class
│   ├── filter.py             # ContentFilter class
├── scripts/
│   ├── run_rufus.py          # Script to execute the crawler
├── crawled_data/             # Folder to store intermediate crawled data
├── filtered_data.json        # Final output after filtering
├── requirements.yaml         # Conda environment dependencies
├── setup.py                  # Project setup for pip installation
└── README.md                 # Project documentation (this file)
```

Setup
-----

To configure the Rufus Crawler, you will need an OpenAI API key.

1.  **OpenAI API Key**: Obtain an API key from [OpenAI](https://platform.openai.com/signup/) if you don't have one.
    
2.  Edit the `run_rufus.py` script to add your OpenAI API key, target URL, and instructions.
    
    In `scripts/run_rufus.py`:
    
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

Example Output
--------------

```json
[
    {
        "URL": "https://www.uta.edu/admissions/apply/graduate",
        "content": "GPT-filtered content related to the admission process."
    },
    {
        "URL": "https://www.uta.edu/admissions/contact",
        "content": "GPT-filtered content providing contact details for admissions."
    }
]
```

Cleaning Up
-----------

After execution, the script automatically deletes the intermediate `.txt` files and directories, leaving only the `filtered_data.json` file with the relevant content.

Known Issues
------------

*   **Dynamic Content**: Some dynamic content may take longer to load, so increasing the sleep time in the `selenium_get_page_content()` method might help if certain content is missing.
*   **Rate Limiting**: OpenAI has rate limits, so ensure you have adequate API limits or handle API exceptions gracefully.

Contributing
------------

Contributions are welcome! If you'd like to contribute to this project, feel free to fork the repository and submit a pull request.

License
-------

This project is licensed under the MIT License.
