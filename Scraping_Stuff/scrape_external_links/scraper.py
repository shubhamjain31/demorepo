# import urllib
# from bs4 import BeautifulSoup
# from urllib.request import urlopen
# from urllib.parse import urlsplit
# import re
# ext = set()
# def getExt(url):
#     o = urllib.parse.urlsplit(url)
#     html = urlopen(url)
#     bs = BeautifulSoup(html, 'html.parser')
#     for link in bs.find_all('a', href = re.compile('^((https://)|(http://))')):
#         if 'href' in link.attrs:
#             if o.netloc in (link.attrs['href']):
#                 continue
#             else:
#                 ext.add(link.attrs['href'])
# getExt('https://www.oreilly.com/online-learning/features.html')
# for i in ext:
#     print(i)

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

import requests, random, time
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup

user_agents = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36 Edg/85.0.564.70',
                'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
                'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
                'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0',
                'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36 Vivaldi/3.3',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36 Vivaldi/3.3']


# initialize the set of links (unique links)
internal_urls = set()
external_urls = set()

def is_valid(url):
    """
    Checks whether `url` is a valid URL.
    """
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

def get_all_website_links(url):
    """
    Returns all URLs that is found on `url` in which it belongs to the same website
    """
    # all URLs of `url`
    urls = set()

    # domain name of the URL without the protocol
    domain_name = urlparse(url).netloc
    try:
        soup = BeautifulSoup(requests.get(url).content, "html.parser", from_encoding="iso-8859-1")

        for a_tag in soup.findAll("a"):
            href = a_tag.attrs.get("href")
            if href == "" or href is None:
                # href empty tag
                continue

            # join the URL if it's relative (not absolute link)
            href = urljoin(url, href)

            parsed_href = urlparse(href)
            # remove URL GET parameters, URL fragments, etc.
            href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path

            if not is_valid(href):
                # not a valid URL
                continue
            if href in internal_urls:
                # already in the set
                continue
            if domain_name not in href:
                # external link
                if href not in external_urls:
                    headers = {"User-Agent": random.choice(user_agents)}

                    try:
                        request_response            = requests.get(href, headers=headers)
                    except:
                        request_response            = ''

                    try:
                        status_code                 = request_response.status_code
                    except:
                        status_code                 = ''

                    website_is_up = status_code < 400 or status_code == 403
                    if website_is_up:
                        status = 'Up'
                    else:
                        status = 'Down'
                    
                    print(href, status_code, status)
                    external_urls.add(href)
                continue
            urls.add(href)
            internal_urls.add(href)
    except Exception as e:
        pass
    return urls

# number of urls visited so far will be stored here
total_urls_visited = 0

def crawl(url, max_urls):
    """
    Crawls a web page and extracts all links.
    You'll find all links in `external_urls` and `internal_urls` global set variables.
    params:
        max_urls (int): number of max urls to crawl, default is 30.
    """
    global total_urls_visited
    total_urls_visited += 1
    links = get_all_website_links(url)
    for link in links:
        if total_urls_visited > max_urls:
            break
        crawl(link, max_urls=max_urls)


# if __name__ == "__main__":
start = time.time()
crawl("https://www.google.com/", 300)
ttime = time.time() - start
print(ttime, 'totaltime')
# print("[+] Total Internal links:", len(internal_urls))
# print("[+] Total External links:", len(external_urls))
# print("[+] Total URLs:", len(external_urls) + len(internal_urls))
# print("[+] Total crawled URLs:", max_urls)