import urllib

from aisearcher import AI
from reader import read_test

urls, contents = read_test()
htmls = []

for i in range(0, len(urls)):
    htmls.append(urllib.urlopen(urls[i]).read())

ai_searcher = AI(htmls, contents)
ai_searcher.get_best_selector()
