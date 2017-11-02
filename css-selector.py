import urllib

from aisearcher import get_best_selector
from reader import read_test

urls, contents = read_test()
htmls = []

for i in range(0, len(urls)):
    htmls.append(urllib.urlopen(urls[i]).read())

get_best_selector(htmls, contents)
