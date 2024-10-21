import requests
from bs4 import BeautifulSoup
import re
import time

class WebCrawler:
    """
    A web crawler class to fetch and extract information from web pages.

    Attributes:
        allow_non_english (bool): Flag to allow non-English content.
        headers (dict): HTTP headers for the requests.

    Methods:
        fetch_page(url, retries=3, delay=5):
            Fetches the HTML content of a web page.
            
            Args:
                url (str): The URL of the web page to fetch.
                retries (int): Number of retries in case of failure. Default is 3.
                delay (int): Delay between retries in seconds. Default is 5.
            
            Returns:
                str: The HTML content of the page if successful, None otherwise.

        extract_text_from_article(html):
            Extracts text content from an article in the HTML.
            
            Args:
                html (str): The HTML content of the web page.
            
            Returns:
                str: The extracted text content from the article.

        extract_novel_info(html):
            Extracts novel information such as title and author from the HTML.
            
            Args:
                html (str): The HTML content of the web page.
            
            Returns:
                tuple: A tuple containing the title and author of the novel. Returns (None, None) if not found.
    """
    
    def __init__(self, allow_non_english: bool = False, headers: dict = None):
        """
        Initializes the WebCrawler with optional parameters.

        Args:
            allow_non_english (bool): Flag to allow non-English content. Default is False.
            headers (dict): HTTP headers for the requests. Default is None.
        """
        self.headers = headers or {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        self.allow_non_english = allow_non_english

    def fetch_page(self, url: str, retries: int = 3, delay: int = 5) -> str:
        """
        Fetches the HTML content of a web page.

        Args:
            url (str): The URL of the web page to fetch.
            retries (int): Number of retries in case of failure. Default is 3.
            delay (int): Delay between retries in seconds. Default is 5.

        Returns:
            str: The HTML content of the page if successful, None otherwise.
        """
        for _ in range(retries):
            response = requests.get(url, headers=self.headers)
            if response.status_code == 200:
                return response.text
            elif response.status_code == 429:
                print(f"Rate limited. Retrying in {delay} seconds...")
                time.sleep(delay)
                delay *= 2  # Exponential backoff
            else:
                print(f"Failed to retrieve the page. Status code: {response.status_code}")
                return None
        return None

    def extract_text_from_article(self, html: str) -> str:
        """
        Extracts text content from an article in the HTML.

        Args:
            html (str): The HTML content of the web page.

        Returns:
            str: The extracted text content from the article.
        """
        soup = BeautifulSoup(html, 'html.parser')
        article_div = soup.find('div', id='article')
        if article_div:
            text_elements = article_div.find_all(['p', 'h4'])
            text = '\n'.join(element.get_text(strip=True) for element in text_elements if not element.find('script'))
            return text.strip()
        return ""

    def extract_novel_info(self, html: str) -> tuple:
        """
        Extracts novel information such as title and author from the HTML.

        Args:
            html (str): The HTML content of the web page.

        Returns:
            tuple: A tuple containing the title and author of the novel. Returns (None, None) if not found.
        """
        soup = BeautifulSoup(html, 'html.parser')
        title_tag = soup.find('meta', property='og:novel:novel_name')
        author_tag = soup.find('meta', property='og:novel:author')
        if title_tag and author_tag:
            title = title_tag.get('content')
            author = author_tag.get('content')
            author = author.split(',')
            authors = []
            if not self.allow_non_english:
                if not re.match(r'^[\x00-\x7F]+$', title):
                    print("Non-English title detected. Skipping...")
                    title = " "
                for auth in author:
                    if not re.match(r'^[\x00-\x7F]+$', auth):
                        print("Non-English author detected. Skipping...")
                    else:
                        authors.append(auth)
            else:
                authors = author
                
            return title, authors
        return None, None