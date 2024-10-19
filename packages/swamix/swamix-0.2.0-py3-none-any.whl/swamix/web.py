import os
import time
import requests
import urllib.parse
from selectolax.parser import HTMLParser

# WEBFN______________________________________
def get_random_proxy():
    import re

    fname = "proxylist.set"
    sourceurl = "https://free-proxy-list.net/"
    cacheTime: "seconds" = 30

    if os.path.exists(fname):
        tdelta = time.time() - os.path.getmtime(fname)
        if tdelta >= cacheTime:
            pass
        else:
            print(f"LOG: using preexisting proxyDB: created {tdelta}s ago ")
            return setload(fname).pop()

    page = get_page(sourceurl)
    iplist = re.findall(r"[\d]+\.[\d]+\.[\d]+\.[\d]+:[\d]+", page.text)
    proxylist = {"http://" + x for x in iplist}
    setwrite(fname, proxylist)
    print("LOG: refreshed proxy list")
    return proxylist.pop()


def make_session_pool(count=1):
    return [requests.Session() for x in range(count)]


UserAgent = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0"}


def get_page(url, **kwargs):  # return a page req object and retrive text later
    if 'headers' not in kwargs:
        kwargs['headers'] = UserAgent
    req = requests.get(url, **kwargs)
    return req


def post_page(url, **kwargs):
    if 'headers' not in kwargs:
        kwargs['headers'] = UserAgent
    r = requests.post(url, **kwargs)
    return r


def parse_html(markup, selector=None):
    # check if markup is a file path
    if os.path.exists(markup):
        markup = fread(markup, encoding='utf-8')

    html = HTMLParser(markup)
    if selector:
        return html.css(selector)
    return html


def get_page_parsed(url, headers={}, selector=None):
    return parse_html(get_page(url, headers=headers).text, selector)


def make_playwright_browser(headless=False):
    from playwright.sync_api import sync_playwright

    playwright = sync_playwright().start()
    browser = playwright.firefox.launch(headless=headless)
    return browser, playwright


def get_page_playwright(
    browser,
    url,
    new_context=False,
    delay=2,
    waitcondition=lambda: True,
    waitcondition_polling=0.2,
    waitcondition_retries=10,
):
    try:
        if new_context:
            context = browser.new_context()
            page = context.new_page()
        else:
            page = browser.new_page()

        page.goto(url)

        retry = 0
        while not waitcondition():
            if retry >= waitcondition_retries:
                break
            time.sleep(waitcondition_polling)
            retry += 1

        return page.content()
    except Exception as e:
        print(repr(e))


def parse_header(*firefoxAllHeaders, file=""):
    if firefoxAllHeaders:
        rawheader = firefoxAllHeaders[0]
    if file:
        rawheader = jload(file)
    serializedHeaders = list((rawheader).values())[0]["headers"]
    return {k: v for k, v in [x.values() for x in serializedHeaders]}


def parse_raw_headers(fpath, log=0):
    headers = {}
    for x in open(fpath).read().split('\n'):
        d = dict([[y.strip() for y in x.split(':', 1)]])
        headers.update(d)
        if log:
            print(d)
    return headers


def make_cookie(req):
    return ";".join([f"{k}={v}" for k, v in req.cookies.items()])


def auto_encoder(d):
    '''encode dict to url get params'''
    string = "&".join([f"{k}={urllib.parse.quote_plus(str(v))}" for k, v in d.items()])
    return string
