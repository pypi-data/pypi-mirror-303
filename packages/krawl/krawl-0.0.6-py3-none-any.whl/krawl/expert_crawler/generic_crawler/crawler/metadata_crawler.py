import asyncio

import aiohttp
from aiohttp import ClientError, ClientTimeout
from bs4 import BeautifulSoup
from pydantic import BaseModel, Field


class Metadata(BaseModel):
    title: str = Field(default='')
    description: str = Field(default='')
    image_url: str = Field(default='')


class PageMeta(BaseModel):
    url: str
    metadata: Metadata = Metadata()
    err: str = Field(default='')


def _mayhave(soup: BeautifulSoup, tag: str):
    try:
        text = soup.find(tag).text
    except Exception:
        text = ''
    return text


def _maybeimage(soup: BeautifulSoup):
    # Apple Touch Icon
    apple_icon = soup.find('link', rel='apple-touch-icon')
    if apple_icon and apple_icon.get('href'):
        return apple_icon['href']

    # General Icon (favicon)
    favicon = soup.find('link', rel='icon')
    if favicon and favicon.get('href'):
        return favicon['href']

    # Find the largest image in the <img> tags
    images = soup.find_all('img')
    if images:
        return images[0].get('source', '')

    return ''


def _get_meta(soup: BeautifulSoup) -> Metadata:
    def _metaprop(prop: str, twitterprop: str) -> str:
        return (
            soup.find('meta', property=prop)['content'] if soup.find('meta', property=prop) else
            soup.find('meta', attrs={'name': twitterprop})['content'] if soup.find('meta', attrs={'name': twitterprop}) else
            ''
        )
    return Metadata(
        title=_metaprop('og:title', 'twitter:title') or _mayhave(
            soup, 'title'),
        description=_metaprop('og:description', 'twitter:description'),
        image=_metaprop('og:image', 'twitter:image') or _maybeimage(soup)
    )


async def fetch_metadata(session, url) -> PageMeta:
    timeout = ClientTimeout(total=3)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    try:
        async with session.get(url, timeout=timeout, allow_redirects=True, headers=headers) as response:
            if response.status == 200:
                html = await response.text()
                soup = BeautifulSoup(html, 'html.parser')
                metadata = _get_meta(soup)
                return PageMeta(url=url, metadata=metadata)
            else:
                print(f'HTTPERR: {response.status}')
                print(response)
                return PageMeta(url=url, err="HTTP_ERR")
    except asyncio.TimeoutError:
        return PageMeta(url=url, err='TIMEOUT')
    except ClientError:
        return PageMeta(url=url, err='ClientErr')  # Page does not exist
    except Exception as err:
        return PageMeta(url=url, err=str(err))


async def process_urls(urls):
    async with aiohttp.ClientSession() as session:
        tasks = []
        semaphore = asyncio.Semaphore(10)  # Limit to 10 concurrent tasks

        async def bounded_fetch(url):
            async with semaphore:
                return await fetch_metadata(session, url)

        for url in urls:
            task = asyncio.ensure_future(bounded_fetch(url))
            tasks.append(task)

        results = await asyncio.gather(*tasks)
        return results


def main(urls):
    loop = asyncio.get_event_loop()
    results = loop.run_until_complete(process_urls(urls))

    for result in results:
        print(f"URL: {result.url}")
        print(f"Title: {result.metadata.title}")
        print(f"Image: {result.metadata.image_url}")
        print(f"Err: {result.err}")
        print("---")


if __name__ == "__main__":
    urls = [
        "https://codepen.io/shshaw/pen/YpERQQ",
        "https://www.python.org",
        "https://www.github.com",
        "https://thisurldoesnotexist.zzz",  # Non-existent domain
        "https://httpstat.us/403",  # Simulates a 403 Forbidden error
        "https://httpstat.us/404",  # Simulates a 404 Not Found error
        "https://httpstat.us/200?sleep=5000",  # Simulates a 5s response
    ]
    urls = [
        "https://venngage.com/blog/organizational-chart-examples/"
    ]
    main(urls)
