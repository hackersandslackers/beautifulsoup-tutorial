"""Application entry point."""
from scraper import scrape_page_metadata
from config import URL

scrape = scrape_page_metadata()

if __name__ == '__main__':
    scrape(URL)
