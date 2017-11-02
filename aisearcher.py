from heapq import heappop, heappush

from bs4 import BeautifulSoup

from parse_html import find_class_id_attribute


class AI:
    htmls = None
    contents = None
    soups = []

    def __init__(self, htmls, contents):
        self.htmls = htmls
        self.contents = contents

    def get_best_selector(self):
        for html in self.htmls:
            soup = BeautifulSoup(html.decode('utf-8'), "html.parser")
            self.soups.append(soup)

        classes, ids, tags = find_class_id_attribute(self.soups[0])

        # for soup, content in zip(self.soups, self.contents):
        #     print self.heuristic(str(soup.select('.item > .full-news > .full-news-text > header > div > h1')[0]), content)

        actions = [' > ', ' ']
        priority_queue = []
        heappush(priority_queue, (self.f('html'), 'html'))
        while len(priority_queue) > 0:
            front = heappop(priority_queue)
            print front[0]
            print front[1]
            for act in actions:
                for tag in tags:
                    cur = front[1] + act + tag
                    print cur
                    if self.is_goal(cur):
                        print "HERE"
                        return cur
                    else:
                        heappush(priority_queue, (self.f(cur), cur))

    @staticmethod
    def heuristic(selected, content):
       # print selected
      #  print content
        content = content.replace('\n', '')
        found = False
        ret = 0
        for tag in selected:
            if str(tag).replace('\n', '').find(content) != -1:
                found = True
            ret += str(tag).count('>')
        if not found:
            return 1000000000
        return ret / 2

    @staticmethod
    def cost(selected):
        ret = 0
        for tag in selected:
            ret += len(tag)
        return ret

    def f(self, selector):
        tot = 0
        for soup, content in zip(self.soups, self.contents):
            tot += self.heuristic(soup.select(selector), content)
         #   tot += self.cost(selector)
        return tot / len(self.soups)

    def is_goal(self, selector):

        for soup, content in zip(self.soups, self.contents):
            if self.heuristic(soup.select(selector), content) > 1:
                return False
        return True

