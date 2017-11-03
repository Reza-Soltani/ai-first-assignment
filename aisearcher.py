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
            soup = BeautifulSoup(html.decode('utf-8'), 'html.parser')
            self.soups.append(soup)

        classes, ids, tags = find_class_id_attribute(self.soups[0])
        actions = [' > ', ' ']
        priority_queue = []
        heappush(priority_queue, (self.f('html'), 'html'))
        last_found = 1000000000
        best_found = 'html'
        while len(priority_queue) > 0:
            front = heappop(priority_queue)
            if front[0] > last_found:
                break
            print 'Expanding ' + front[1]
            print 'Cost is: ' + str(front[0])
            last_found = front[0]
            best_found = front[1]
            for act in actions:
                for tag in tags:
                    cur = front[1] + act + tag
                    if self.is_goal(cur):
                        return cur, self.f(cur)
                    else:
                        xx = self.f(cur)
                        if xx <= last_found:
                            heappush(priority_queue, (xx, cur))
                for cls in classes:
                    if cls is not None and len(cls) > 0:
                        cur = front[1] + act + '.' + cls
                        if self.is_goal(cur):
                            return cur, self.f(cur)
                        else:
                            xx = self.f(cur)
                            if xx <= last_found:
                                heappush(priority_queue, (xx, cur))
            if front[1][-1] != ')':
                for i in range(1, 5):
                    cur = front[1] + ":nth-of-type(" + str(i) + ")"
                    if self.is_goal(cur):
                        return cur, self.f(cur)
                    else:
                        xx = self.f(cur)
                        if xx <= last_found:
                            heappush(priority_queue, (xx, cur))
        return best_found, last_found

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

    @staticmethod
    def heuristic_goal(selected, content):
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
        return tot / len(self.soups)

    def is_goal(self, selector):

        for soup, content in zip(self.soups, self.contents):
            if self.heuristic_goal(soup.select(selector), content) > 1:
                return False
        return True

