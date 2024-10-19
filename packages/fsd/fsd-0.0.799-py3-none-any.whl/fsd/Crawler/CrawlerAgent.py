import time
import json
import os
import re
import logging
from firecrawl import FirecrawlApp
from bs4 import BeautifulSoup
import markdown

logger = logging.getLogger(__name__)

class CrawlerAgent:
    def __init__(self, api_key):
        self.api_key = api_key
        env = os.environ.get(
        "FIRECRAWL_LOGGING_LEVEL", "INFO"
        ).upper()
        self.app = FirecrawlApp(api_key=self.api_key)

    def crawl_website(self, website_url, format='markdown'):
        # Set up crawl parameters
        params = {
            'limit': 1,  # Maximum number of pages to crawl
            'scrapeOptions': {
                'formats': [format.lower()]
            },
            # Add other parameters as needed
        }

        try:
            # Start the crawl asynchronously on the server
            crawl_status = self.app.async_crawl_url(website_url, params=params)
            crawl_id = crawl_status.get('id')
            if not crawl_id:
                logger.debug("\n #### The `CrawlerAgent` failed to initiate the crawl: No crawl ID was returned.")
                return None
            logger.info(" #### The `CrawlerAgent` has commenced the reading process!")

            # Poll for the crawl status
            while True:
                status = self.app.check_crawl_status(crawl_id)
                logger.info(f"\n #### The `CrawlerAgent` reports current reading status: `{status.get('status')}`")
                if status.get('status') == 'completed':
                    break
                elif status.get('status') == 'failed':
                    logger.debug("\n #### The `CrawlerAgent` reports that the reading process has failed.")
                    return None
                time.sleep(2.5)  # Wait 5 seconds before checking again

            # Retrieve the crawl results
            final_status = self.app.check_crawl_status(crawl_id)
            results = final_status.get('data')
            if results:
                return results
            else:
                logger.debug("\n #### The `CrawlerAgent` was unable to retrieve the reading results.")
                return None

        except Exception as e:
            logger.debug(f" #### The `CrawlerAgent` encountered an error during the reading process: `{e}`")
            return None

    def process(self, website_url, format='markdown'):
        # Validate and set the format
        if format.lower() not in ['html', 'markdown']:
            logger.debug(f" #### The `CrawlerAgent` detected an invalid format '`{format}`'. Defaulting to markdown.")
            format = 'markdown'

        # Crawl the website
        results = self.crawl_website(website_url, format)
        if results is None:
            logger.debug("\n #### The `CrawlerAgent` reports that the crawling process has failed.")
            return None

        return results
