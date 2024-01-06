"""Scraper configuration."""
from os import getenv, path

from dotenv import load_dotenv

# Load variable from .env
BASE_DIR: str = path.abspath(path.dirname(__file__))
load_dotenv(path.join(BASE_DIR, ".env"))

# Fetch URL to scrape via environment variable
TARGET_URL = getenv("TARGET_URL")
