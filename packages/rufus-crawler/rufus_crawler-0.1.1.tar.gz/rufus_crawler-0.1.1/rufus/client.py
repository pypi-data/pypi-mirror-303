# rufus/client.py
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import json
import re
import openai
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager  # For automatic ChromeDriver management
import time
import shutil  # To delete intermediate files

class RufusClient:
    def __init__(self, openai_api_key, base_folder="crawled_data"):
        self.openai_api_key = openai_api_key
        openai.api_key = self.openai_api_key
        self.base_folder = base_folder
        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)
        os.environ["TOKENIZERS_PARALLELISM"] = "false"  # Avoid parallelism issues in tokenizers

        # Set up Selenium WebDriver (Headless Chrome)
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run headless Chrome (without GUI)
        chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration
        chrome_options.add_argument("--no-sandbox")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    def save_to_txt(self, url, content, depth):
        """
        Saves the content of each URL into a .txt file.
        """
        folder = os.path.join(self.base_folder, f"depth_{depth}")
        if not os.path.exists(folder):
            os.makedirs(folder)
        
        # Create a valid filename from the URL
        filename = re.sub(r'[^\w\-_\. ]', '_', url) + ".txt"
        filepath = os.path.join(folder, filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Saved content from {url} to {filepath}")

    def dynamic_extract_content(self, html):
        """
        Extract the main text content from the page's HTML.
        """
        soup = BeautifulSoup(html, "html.parser")
        return soup.get_text(separator=' ', strip=True)

    def selenium_get_page_content(self, url):
        """
        Uses Selenium to fetch the dynamic content of a webpage rendered by JavaScript.
        """
        self.driver.get(url)
        time.sleep(3)  # Wait for JavaScript to load (adjust sleep time as needed)
        return self.driver.page_source

    def crawl(self, url, depth=2):
        """
        Crawls the given URL, saves the content into .txt files, and traverses additional links up to the specified depth.
        """
        visited = set()  # To avoid revisiting the same page
        def crawl_page(current_url, current_depth):
            if current_depth > depth or current_url in visited:
                return
            visited.add(current_url)
            
            # Skip invalid URLs like tel:, javascript:, mailto:
            if re.match(r'^(tel:|javascript:|mailto:|#)', current_url):
                print(f"Skipping invalid URL: {current_url}")
                return
            
            try:
                # Fetch the page content using Selenium (JavaScript-rendered content)
                html_content = self.selenium_get_page_content(current_url)

                # Extract content from the page
                content = self.dynamic_extract_content(html_content)

                # Save content to txt file
                self.save_to_txt(current_url, content, current_depth)

                # Find all links and crawl them
                soup = BeautifulSoup(html_content, "html.parser")
                links = soup.find_all("a", href=True)
                for link in links:
                    href = link['href']
                    next_url = urljoin(current_url, href)
                    crawl_page(next_url, current_depth + 1)

            except Exception as e:
                print(f"Error crawling {current_url}: {e}")

        crawl_page(url, 1)

    def convert_txt_to_json(self, output_file="crawled_data.json"):
        """
        Convert the saved text files into a JSON file with URL and content.
        """
        crawled_data = []

        # Traverse through the directories and read all .txt files
        for depth_folder in os.listdir(self.base_folder):
            depth_path = os.path.join(self.base_folder, depth_folder)
            if os.path.isdir(depth_path):
                for txt_file in os.listdir(depth_path):
                    if txt_file.endswith(".txt"):
                        file_path = os.path.join(depth_path, txt_file)
                        with open(file_path, 'r', encoding='utf-8') as f:
                            content = f.read()
                        # Recreate the URL from the filename
                        url = txt_file.replace('_', '/').replace('.txt', '')
                        crawled_data.append({
                            "URL": url,
                            "content": content
                        })

        # Save as JSON
        with open(output_file, "w") as f:
            json.dump(crawled_data, f, indent=4)
        print(f"Crawled data saved to {output_file}")
        return crawled_data

    def cleanup_files(self):
        """
        Delete all intermediate files and folders, keeping only the final JSON file.
        """
        try:
            shutil.rmtree(self.base_folder)  # Delete the base folder with all txt files
            print(f"Deleted intermediate files in {self.base_folder}")
        except Exception as e:
            print(f"Error deleting files: {e}")
