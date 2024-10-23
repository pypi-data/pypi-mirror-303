# Importing required modules
import requests
from bs4 import BeautifulSoup
import urllib
import asyncio
import aiohttp
from tqdm import tqdm
import nest_asyncio
nest_asyncio.apply()
import uuid 


# Mapping HTTP response status codes to their meanings
httpResponseStatusCodes = {
    100 : 'Continue',
    101 : 'Switching Protocol',
    102 : 'Processing (WebDAV)',
    103 : 'Early Hints',
    200 : 'Success',
    201 : 'Created',
    202 : 'Accepted',
    203 : 'Non-Authoritative Information',
    204 : 'No Content',
    205 : 'Reset Content',
    206 : 'Partial Content',
    207 : 'Multi-Status (WebDAV)',
    208 : 'Already Reported (WebDAV)',
    226 : 'IM Used (HTTP Delta encoding)',
    300 : 'Multiple Choice',
    301 : 'Moved Permanently',
    302 : 'Found',
    303 : 'See Other',
    304 : 'Not Modified',
    305 : 'Use Proxy',
    306 : 'Unused',
    307 : 'Temporary Redirect',
    308 : 'Permanent Redirect',
    400 : 'Bad Request',
    401 : 'Unauthorized',
    402 : 'Payment Required',
    403 : 'Forbidden',
    404 : 'Not Found',
    405 : 'Method Not Allowed',
    406 : 'Not Acceptable',
    407 : 'Proxy Authentication Required',
    408 : 'Request Timeout',
    409 : 'Conflict',
    410 : 'Gone',
    411 : 'Length Required',
    412 : 'Precondition Failed',
    413 : 'Payload Too Large',
    414 : 'URI Too Long',
    415 : 'Unsupported Media Type',
    416 : 'Range Not Satisfiable',
    417 : 'Expectation Failed',
    418 : 'I am a teapot',
    421 : 'Misdirected Request',
    422 : 'Unprocessable Entity (WebDAV)',
    423 : 'Locked (WebDAV)',
    424 : 'Failed Dependency (WebDAV)',
    425 : 'Too Early',
    426 : 'Upgrade Required',
    428 : 'Precondition Required',
    429 : 'Too Many Requests',
    431 : 'Request Header Fields Too Large',
    451 : 'Unavailable For Legal Reasons',
    500 : 'Internal Server Error',
    501 : 'Not Implemented',
    502 : 'Bad Gateway',
    503 : 'Service Unavailable',
    504 : 'Gateway Timeout',
    505 : 'HTTP Version Not Supported',
    506 : 'Variant Also Negotiates',
    507 : 'Insufficient Storage (WebDAV)',
    508 : 'Loop Detected (WebDAV)',
    510 : 'Not Extended',
    511 : 'Network Authentication Required'
}

# Class for Bing Search Scraper
class BingScraper():
    # Default headers for the scraper
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}

    def __init__(self,headers=headers, max_retries=3, num_results=10):
        """
        Initializes a BingScraper object.

        Args:
            headers: Optional dictionary of headers to use for HTTP requests. If not provided, a default set of headers will be used.
            max_retries: The maximum number of retries for failed requests (default: 3).
            num_results: The maximum number of results to get (default: 10)
        """
        self.headers = headers
        self.max_retries = max_retries
        self.num_results = num_results
        self.retries = 0

    def get_results(self, q):
        """
        Fetches Bing search results for the given query.

        Args:
            q: The query string to search for.

        Returns:
            A dictionary containing the following keys:
                - query: The original query string.
                - organic_results: A list of organic search result dictionaries, where each dictionary contains:
                    - position: The position of the result in the list.
                    - source: The source of the result (e.g., website name).
                    - title: The title of the result.
                    - link: The URL of the result.
                    - summary: A short summary of the result.
                - number_of_results: The total number of organic results found.
                - status: The HTTP response status code.
        """

        q_encode=urllib.parse.quote_plus(q)
        url = f'https://www.bing.com/search?q={q_encode}&qs=n&form=QBRE&sp=-1&lq=0&pq=&sc=0-0&sk=&cvid={uuid.uuid4().hex.upper()}&ghsh=0&ghacc=0&ghpl='
        res = requests.get(url, headers=self.headers)
        self.retries += 1

        results = {'query':url, 'organic_results':list(dict()), 'status':httpResponseStatusCodes.get(res.status_code)}
        if res.status_code == 200:
            soup = BeautifulSoup(res.content, "html.parser")
            if soup.find('ol',id="b_results"):
                for pos, elm in enumerate(soup.find('ol',id="b_results").find_all('li',class_='b_algo')):
                    source = title = link = summary = None
                    if elm.find('div',class_="tptt"):
                        source = elm.find('div',class_="tptt").text
                    if elm.find('h2'):
                        title = elm.find('h2').text
                        if elm.find('h2').find('a'):
                            link = elm.find('h2').find('a')['href']
                    if elm.find('p'):
                        summary = elm.find('p').text
                    results['organic_results'].append({'position':pos+1, 'source':source, 'title':title, 'link':link, 'summary':summary})
                    if pos+1 == self.num_results:
                        break
            results['number_of_results'] = len(results['organic_results'])
        elif self.retries < self.max_retries:
            results = self.get_results(q)
        return results
    
class AsyncBingScraper:
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}

    def __init__(self, headers=headers, max_retries=3, num_results=10, error_sleep = 1, hits_at_a_time=30):
        """
        Initializes an AsyncBingScraper object.

        Args:
            headers: Optional dictionary of headers to use for HTTP requests. If not provided, a default set of headers will be used.
            max_retries: The maximum number of retries for failed requests (default: 3).
            num_results: The maximum number of results to get (default: 10)
            error_sleep: Time to sleep if the result not get or status not 200 (default: 1)
            hits_at_a_time: Number of hits at a time (default: 30)
        """
        self.headers = headers
        self.max_retries = max_retries
        self.num_results = num_results
        self.error_sleep = error_sleep
        self.hits_at_a_time = hits_at_a_time

    async def _fetch_results(self, semaphore, session, q, pbar, retries=0):
        q_encode = urllib.parse.quote_plus(q)
        url = f'https://www.bing.com/search?q={q_encode}&qs=n&form=QBRE&sp=-1&lq=0&pq=&sc=0-0&sk=&cvid={uuid.uuid4().hex.upper()}&ghsh=0&ghacc=0&ghpl='
        async with semaphore:
            try:
                async with session.get(url, headers=self.headers, read_until_eof=False) as response:
                    if response.status == 200:
                        content = await response.text()
                        pbar.update(1)
                        return url, content, response.status
                    elif retries < self.max_retries:
                        await asyncio.sleep(self.error_sleep)
                        return await self._fetch_results(semaphore, session, q, pbar, retries=retries + 1)
                    else:
                        pbar.update(1)
                        return url, None, response.status
            except:
                return await self._fetch_results(semaphore, session, q, pbar, retries=retries)

    async def _parse_html_content(self, query, html_content, status, pbar):
        result_data = {'query': query, 'organic_results': list(), 'status': httpResponseStatusCodes.get(status)}

        if html_content:
            soup = BeautifulSoup(html_content, "lxml")
            b_results = soup.find('ol', id="b_results")
            if b_results:
                for pos, elm in enumerate(b_results.find_all('li', class_='b_algo', limit=self.num_results)):
                    source = title = link = summary = None
                    if elm.find('div', class_="tptt"):
                        source = elm.find('div', class_="tptt").text
                    if elm.find('h2'):
                        title = elm.find('h2').text
                        if elm.find('h2').find('a'):
                            link = elm.find('h2').find('a')['href']
                    if elm.find('p'):
                        summary = elm.find('p').text
                    result_data['organic_results'].append({'position': pos + 1, 'source': source, 'title': title, 'link': link, 'summary': summary})
                    if pos + 1 == self.num_results:
                        break

            result_data['number_of_results'] = len(result_data['organic_results'])
        pbar.update(1)
        return result_data

    async def _collect_results(self, queries):
        async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=10)) as session:
            pbar = tqdm(total=len(queries), desc="Extracting Queries")
            semaphore = asyncio.Semaphore(self.hits_at_a_time)
            tasks = [self._fetch_results(semaphore=semaphore, session=session, q=query, pbar=pbar) for query in queries]
            results = await asyncio.gather(*tasks)
            pbar.close()

            pbar = tqdm(total=len(results), desc="Converting Queries")
            tasks = [self._parse_html_content(query, html_content, status, pbar) for query, html_content, status in results]
            formatted_results = await asyncio.gather(*tasks)
            pbar.close()
        return formatted_results

    def get_results(self, queries):
        """
        Fetches Bing search results for a given list of queries asynchronously.

        Args:
            queries: A list of query strings to search for.

        Returns:
            A list of dictionaries, where each dictionary contains the search results and status information for a corresponding query. Each dictionary contains the following keys:

            - query: The original query string.
            - organic_results: A list of organic search result dictionaries, where each
               dictionary contains:
                 - position: The position of the result in the list.
                 - source: The source of the result (e.g., website name).
                 - title: The title of the result.
                 - link: The URL of the result.
                 - summary: A short summary of the result.
            - number_of_results: The total number of organic results found.
            - status: The HTTP response status code.
        """
        return asyncio.run(self._collect_results(queries))