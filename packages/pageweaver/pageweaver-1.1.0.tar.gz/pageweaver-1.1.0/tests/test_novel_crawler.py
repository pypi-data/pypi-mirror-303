import unittest
import os
from pageweaver.text_processor import TextProcessor
from pageweaver.document_generator import DocumentGenerator
from pageweaver.novel_crawler_service import NovelCrawlerService
from pageweaver.web_crawler import WebCrawler

class TestNovelCrawler(unittest.TestCase):
    def test_fetch_page(self):
        crawler = WebCrawler()
        html = crawler.fetch_page('https://example.com')
        self.assertIsNotNone(html)

    def test_remove_non_utf8_characters(self):
        processor = TextProcessor()
        text = "Hello, world \x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0A\x0B\x0C\x0D\x0E\x0F\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1A\x1B\x1C\x1D\x1E\x1F\x7F"
        cleaned_text = processor.remove_non_utf8_characters(text)
        self.assertEqual(cleaned_text, "Hello, world ")

    def test_generate_pdf(self):
        generator = DocumentGenerator(title="Test Title", author="Test Author")
        generator.add_chapter("Test Chapter", "This is a test content.")
        generator.generate_pdf("/tmp/test_document", clean_tex=True)
        self.assertTrue(os.path.exists("/tmp/test_document.pdf"))

    def test_crawl_novel(self):
        service = NovelCrawlerService(
            novel_url='https://freewebnovel.com/global-fog-survival.html',
            start_chapter=1,
            end_chapter=2,
            output_dir='/tmp',
            num_workers=6
        )
        service.crawl_novel()
        self.assertTrue(os.path.exists("/tmp/Global Fog Survival.pdf"))

if __name__ == '__main__':
    unittest.main()
