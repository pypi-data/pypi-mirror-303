import time
import random
import argparse
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from langdetect import detect, LangDetectException
from .web_crawler import WebCrawler
from .text_processor import TextProcessor
from .document_generator import DocumentGenerator

class NovelCrawlerService:
    def __init__(self, novel_url: str, start_chapter: int, end_chapter: int, output_dir: str, num_workers: int, allow_non_english: bool = False) -> None:
        """
        Initialize the NovelCrawlerService.

        :param novel_url: URL of the novel to crawl.
        :param start_chapter: Starting chapter number.
        :param end_chapter: Ending chapter number.
        :param output_dir: Directory to save the generated PDF.
        :param num_workers: Number of workers for concurrent crawling.
        :param allow_non_english: Allow non-English characters in the novel title and author name.
        """
        self.novel_url = novel_url
        self.start_chapter = start_chapter
        self.end_chapter = end_chapter
        self.output_dir = output_dir
        self.num_workers = num_workers
        self.allow_non_english = allow_non_english
        self.crawler = WebCrawler(self.allow_non_english)
        self.processor = TextProcessor()
        self.title, self.authors, self.base_url = self.extract_novel_info()
        if not self.title or not self.authors or not self.base_url:
            raise ValueError("Failed to extract novel title, authors, or base URL.")

        # Detect language for title and authors
        if self.allow_non_english:
            title_lang = self.detect_language(self.title) if self.title else 'en'
            author_langs = [self.detect_language(author) if author else 'en' for author in self.authors]
        else:
            title_lang = 'en'
            author_langs = ['en'] * len(self.authors)
        self.doc_generator = DocumentGenerator(self.title, self.authors, title_lang, author_langs)

    def extract_novel_info(self) -> tuple[str, list[str], str]:
        """
        Extract novel information such as title, authors, and base URL.

        :return: A tuple containing the title, authors, and base URL.
        """
        html = self.crawler.fetch_page(self.novel_url)
        if html:
            title, authors = self.crawler.extract_novel_info(html)
            base_url = self.novel_url.replace('https://freewebnovel.com', 'https://read.freewebnovel.me')
            base_url = base_url.replace('.html', '')
            return title, authors, base_url
        return None, None, None

    def detect_language(self, text: str) -> str:
        """
        Detect the language of a given text.

        :param text: Text to detect the language of.
        :return: Detected language code.
        """
        try:
            lang = detect(text)
            if lang == 'zh-cn':
                return 'cn'
            elif lang == 'ja':
                return 'jp'
            return lang
        except LangDetectException:
            return 'en'

    def process_chapter(self, current_chapter: int) -> tuple[int, str, list[str], str]:
        """
        Process a single chapter by crawling, extracting text, and detecting language.

        :param current_chapter: Chapter number to process.
        :return: A tuple containing chapter number, heading, paragraphs, and language.
        """
        MIN_SENTENCES_PER_PARAGRAPH = 20
        MAX_SENTENCES_PER_PARAGRAPH = 25

        current_url = f"{self.base_url}/chapter-{current_chapter}"
        html = self.crawler.fetch_page(current_url)
        if html:
            text = self.crawler.extract_text_from_article(html)
            if text:
                text = self.processor.remove_non_utf8_characters(text)
                chapter_heading = f"Chapter {current_chapter}"
                text = text.replace(chapter_heading, '', 1).strip()

                # Split text into sentences based on periods
                sentences = text.split('. ')

                # Group sentences into paragraphs
                paragraphs = []
                current_paragraph = []
                for sentence in sentences:
                    current_paragraph.append(sentence)
                    if len(current_paragraph) >= random.randint(MIN_SENTENCES_PER_PARAGRAPH, MAX_SENTENCES_PER_PARAGRAPH):
                        paragraphs.append('. '.join(current_paragraph).strip() + '.')
                        current_paragraph = []
                if current_paragraph:
                    paragraphs.append('. '.join(current_paragraph).strip() + '.')

                lang = self.detect_language(text)
                return current_chapter, chapter_heading, paragraphs, lang
            else:
                print(f"Chapter {current_chapter} not found.")
        else:
            print(f"Failed to fetch {current_url}")
        return None

    def crawl_novel(self) -> None:
        """
        Crawl the novel from start to end chapter and generate a PDF.
        """
        with ThreadPoolExecutor(max_workers=self.num_workers) as executor:
            futures = []
            for current_chapter in range(self.start_chapter, self.end_chapter + 1):
                futures.append(executor.submit(self.process_chapter, current_chapter))
                time.sleep(random.uniform(0.5, 1.5))

            results = []
            for future in as_completed(futures):
                result = future.result()
                if result:
                    results.append(result)

        results.sort(key=lambda x: x[0])

        for result in results:
            chapter_number, chapter_heading, paragraphs, lang = result
            self.doc_generator.add_chapter(chapter_heading, paragraphs, lang)

        output_file = os.path.join(self.output_dir, self.title)
        self.doc_generator.generate_pdf(output_file, clean_tex=True)

def main() -> None:
    """
    Main function to parse arguments and start the novel crawling service.
    """
    parser = argparse.ArgumentParser(description="Crawl a web novel and generate a PDF.")
    parser.add_argument('novel_url', type=str, help='The FreeWebNovel URL of the novel to crawl.')
    parser.add_argument('start_chapter', type=int, help='The starting chapter number.')
    parser.add_argument('end_chapter', type=int, help='The ending chapter number.')
    parser.add_argument('--output_dir', type=str, default=os.getcwd(), help='The destination directory for the generated PDF.')
    parser.add_argument('--num-workers', type=int, default=10, help='The number of workers to use for crawling.')
    parser.add_argument('--allow-non-english', action='store_true', help='Allow non-English characters in the novel title and author name.')
    args = parser.parse_args()
    print("Output directory: ", args.output_dir)
    service = NovelCrawlerService(args.novel_url, args.start_chapter, args.end_chapter, args.output_dir, args.num_workers, args.allow_non_english)
    service.crawl_novel()

if __name__ == "__main__":
    main()