import urllib

from aisearcher import AI
from reader import read_test

urls, contents = read_test()
htmls = []

for i in range(0, len(urls)):
    htmls.append(urllib.urlopen(urls[i]).read())

ai_searcher = AI(htmls, contents)
find_best = ai_searcher.get_best_selector()
print 'Best founded selector is: ' + find_best[0]
print 'With cost: ' + str(find_best[1])
