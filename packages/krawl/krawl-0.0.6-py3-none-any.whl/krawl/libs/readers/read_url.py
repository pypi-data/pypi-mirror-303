from dataclasses import dataclass
from typing import List, Optional

from bs4 import BeautifulSoup, Tag
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@dataclass
class TaggedText:
    tag: str
    text: str
    url: Optional[str] = ""       # Optional for href
    source: Optional[str] = ""    # Optional for image


@dataclass
class HtmlFetched:
    text: str
    taggedtext: List[TaggedText]
    html: str


class SeleniumBrower:
    def __init__(self, headless: bool = True):
        """

        Parameters
        ----------
        headless : bool, optional
            _description_, by default True


        Example
        -------
        >>> url = "https://getimg.ai/models/flux"
        >>> browser = SeleniumBrower()
        >>> fetched = browser.read(url)
        >>> print("Visible Text:")
        >>> print(fetched.text)
        """
        print("INIT Selenium ...")
        self.chrome_options = Options()
        if headless:
            self.chrome_options.add_argument("--headless")
        self.chrome_options.add_argument("--disable-gpu")
        self.chrome_options.add_argument("--no-sandbox")
        self.chrome_options.add_argument("--disable-dev-shm-usage")
        self.chrome_options.add_argument("--enable-javascript")
        self.driver = webdriver.Chrome(options=self.chrome_options)

    def __del__(self):
        self.driver.quit()

    def read_html(self, url: str) -> HtmlFetched:

        try:
            # Navigate to the URL and wait
            self.driver.get(url)
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "body")))
            # WebDriverWait(self.driver, 20).until(lambda driver: driver.execute_script("return document.readyState") == "complete")
            # WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "main")))

            # Get the page source after JavaScript execution
            page_source = self.driver.page_source
            return page_source
        finally:
            # Close this page
            # driver.quit()
            self.driver.get("about:blank")

    def read(self, url: str) -> HtmlFetched:
        page_source = self.read_html(url)
        soup = BeautifulSoup(page_source, 'html.parser')

        # Remove script and style elements
        for script in soup(["script", "style"]):
            script.decompose()

        # Get text
        taggedtext = extract_visible_text(soup)
        text = soup.get_text()
        # chunks = (phrase.strip()
        #           for line in text.splitlines()
        #           for phrase in line.split("  "))
        # text = '\n'.join(chunk for chunk in chunks if chunk)
        return HtmlFetched(text, taggedtext, page_source)


def extract_visible_text(element: Tag) -> List[TaggedText]:
    # if element.name in ['script', 'style', 'head', 'title', 'meta', '[document]']:
    if element.name in ['script', 'style', 'head', 'meta', '[document]']:
        return []

    result = []
    if element.name is not None and element.string and element.string.strip():
        result.append(TaggedText(element.name,
                                 element.string.strip(),
                                 element.get("href"),
                                 element.get("source")
                                 ))

    for child in element.children:
        if child.name is not None:
            result.extend(extract_visible_text(child))

    return result


if __name__ == "__main__":
    url = "..."
    browser = SeleniumBrower()
    fetched = browser.read(url)
    print("Visible Text:")
    print(fetched.text)
