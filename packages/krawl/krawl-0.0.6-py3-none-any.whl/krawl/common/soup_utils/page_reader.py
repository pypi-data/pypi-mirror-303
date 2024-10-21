from typing import Dict

import requests
from bs4 import BeautifulSoup
from retrying import retry

from krawl.libs.readers.read_url import SeleniumBrower


@retry(wait_exponential_multiplier=320,
       wait_exponential_max=2600,
       stop_max_attempt_number=1)
def fetch_url(
    url: str,
    headers: Dict
):
    """
    Define a decorator for retrying network requests with exponential backoff
    """

    # (sec connection timeout, sec read timeout)
    response = requests.get(url, timeout=(1, 2), headers=headers)

    # session = requests.Session()
    # response = session.get(url)
    response.raise_for_status()

    return response


class HtmlPageReader:
    headers = Dict

    def __init__(self) -> None:
        self.browser = SeleniumBrower()
        self.retry_policy = ""
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (CPU OS 3_2 like Mac OS X; Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
            # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0',
            'Accept-Language': 'en-US,en;q=0.9',
            # 'Referer': 'https://www.google.com/',
            # 'Accept-Encoding': 'gzip, deflate, br',
            # 'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            # 'DNT': '1',  # Do Not Track Request Header
        }
        # http://username:password@your_proxy_ip:your_proxy_port
        # proxies = {
        #     'http': 'http://your_proxy_ip:your_proxy_port',
        #     'https': 'https://your_proxy_ip:your_proxy_port',
        # }

    @staticmethod
    def parse_html(html_content: str) -> BeautifulSoup:
        soup = BeautifulSoup(html_content, 'html.parser')
        return soup

    def get_soup(self, url: str) -> BeautifulSoup:

        try:
            print(f"Fetching {url}")
            response = fetch_url(url, headers=self.headers)
            html_content = response.text
            soup = HtmlPageReader.parse_html(html_content=html_content)
            return soup
        except requests.HTTPError as http_err:
            # 4xx, 5xx
            print(f"    😡 REQUEST-HTTPERR: {http_err}")
            return http_err.response.status_code
        except requests.exceptions.Timeout as err:
            print(f"    😡 REQUEST-TIMOUT: {err}")
            return 999
        except requests.exceptions.RequestException as err:
            # No connection
            print(f"    😡 REQUEST-EXP: {err}")
            return 999
        except Exception as err:
            print(f"    😡 REQUEST-ERR: {err}")
            return None

    def get_soup_heavy(self, url: str, reason: str = "") -> BeautifulSoup:
        input(f"HEAVYFetching {url} | {reason}")
        html_content = self.browser.read_html(url)
        soup = HtmlPageReader.parse_html(html_content=html_content)
        return soup
