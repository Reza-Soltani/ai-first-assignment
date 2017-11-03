from heapq import heappop, heappush

from bs4 import BeautifulSoup

from parse_html import find_class_id_attribute


class AI2:
    htmls = None
    contents = None
    soups = []
    match = ""

    def __init__(self, htmls, contents):
        self.htmls = htmls
        self.contents = contents

    def check_children(self, tag, father):
        for soup in self.soups:
            check = str(soup.select(father)).find(tag)
            if check == -1:
                return False
        return True

    def get_best_selector(self):
        for html in self.htmls:
            soup = BeautifulSoup(html.decode('utf-8'), 'html.parser')
            self.soups.append(soup)

        classes, ids, tags = find_class_id_attribute(self.soups[0])
        for i in range(0,classes.__len__()):
            classes[i] = "." + classes[i]
        all = tags + classes

        actions = [' > ', ' ']
        priority_queue = []
        depth = 0
        heappush(priority_queue, (self.f('html'), 'html'))
        while len(priority_queue) > 0 and depth < 20:
            front = heappop(priority_queue)
            # print "while", front[0], front[1]
            self.match = front[1]
            push = False
            for act in actions:
                for al in all:
                    if True:
                        cur = front[1] + act + al
                        exact_front = [1, 1]
                        try:
                            exact_front = heappop(priority_queue)
                            heappush(priority_queue, (exact_front[0], exact_front[1]))
                        except:
                            exact_front[0] = front[0]

                        f = self.f(cur)
                        if f < exact_front[0]:
                            # print "push", f, cur
                            heappush(priority_queue, (f, cur))
                            push = True
            print priority_queue.__len__()
        print self.match

    @staticmethod
    def heuristic(selected, content):
        content = content.replace('\n', '')
        found = False
        ret = 0
        for tag in selected:
            if str(tag).replace('\n', '').find(content) != -1:
                found = True
                ret += len(str(tag).replace('\n', '')) - len(content)
            else:
                ret += len(str(tag).replace('\n', ''))
        if not found:
            return 1000000000
        return ret

    def f(self, selector):
        tot = 0
        for soup, content in zip(self.soups, self.contents):
            tot += self.heuristic(soup.select(selector), content)
        return tot / len(self.soups)


