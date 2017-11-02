from bs4 import BeautifulSoup


def get_ids(htmls):
    return ['', '', '']


def get_best_selector(htmls, contents):
    soups = []
    for html in htmls:
        soup = BeautifulSoup(html.decode('utf-8'), "html.parser")
        soups.append(soup)

    for soup, content in zip(soups, contents):
        heuristic(str(soup.select('.item > .full-news > .full-news-text > header > div > h1')), content)


def heuristic(selected, content):
    print selected.decode('utf-8')
    print "WTF"
    print "asdasdasads" + content.decode('utf-8')
    print "WTH"


def whatisthis(s):
    if isinstance(s, str):
        print "ordinary string"
    elif isinstance(s, unicode):
        print "unicode string"
    else:
        print "not a string"