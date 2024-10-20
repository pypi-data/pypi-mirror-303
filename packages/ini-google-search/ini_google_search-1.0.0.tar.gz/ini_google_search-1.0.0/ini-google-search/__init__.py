from time import sleep
from bs4 import BeautifulSoup
from requests import get


def _req(term, results, lang, start, proxies, timeout, safe, ssl_verify, region):
    resp = get(
        url="https://www.google.com/xhtml/search",
        headers={
            "sec-ch-ua-platform": '"Linux"',
            "Referer": "https://ogs.google.com/",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
            "sec-ch-ua": '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
            "sec-ch-ua-mobile": "?0",
        },
        params={
            "q": term,
            "num": results + 2,
            "hl": lang,
            "start": start,
            "safe": safe,
            "gl": region,
        },
        proxies=proxies,
        timeout=timeout,
        verify=ssl_verify,
    )
    resp.raise_for_status()
    return resp


class SearchResult:
    def __init__(self, url, title, description):
        self.url = url
        self.title = title
        self.description = description

    def __repr__(self):
        return f"SearchResult(url={self.url}, title={self.title}, description={self.description})"


def search(
    term,
    num_results=10,
    lang="en",
    proxy=None,
    advanced=False,
    sleep_interval=0,
    timeout=5,
    safe="active",
    ssl_verify=None,
    region=None,
    start_num=0,
    unique=False,
):

    proxies = (
        {"https": proxy, "http": proxy}
        if proxy and (proxy.startswith("https") or proxy.startswith("http"))
        else None
    )

    start = start_num
    fetched_results = 0
    fetched_links = set()

    while fetched_results < num_results:

        resp = _req(
            term,
            num_results - start,
            lang,
            start,
            proxies,
            timeout,
            safe,
            ssl_verify,
            region,
        )

        soup = BeautifulSoup(resp.text, "html.parser")
        result_block = soup.find_all("div", attrs={"class": "g"})
        new_results = 0

        for result in result_block:

            link = result.find("a", href=True)
            title = result.find("h3")
            description_box = result.find("div", {"style": "-webkit-line-clamp:2"})

            if link and title and description_box:
                link = result.find("a", href=True)
                if link["href"] in fetched_links and unique:
                    continue
                fetched_links.add(link["href"])
                description = description_box.text
                fetched_results += 1
                new_results += 1
                if advanced:
                    yield SearchResult(link["href"], title.text, description)
                else:
                    yield link["href"]

            if fetched_results >= num_results:
                break

        if new_results == 0:

            break

        start += 10
        sleep(sleep_interval)
