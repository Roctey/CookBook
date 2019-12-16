import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Item({!r})'.format(self.name)

q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)
print(q.pop())  # Item('bar')
print(q.pop())  # Item('spam')
print(q.pop())  # Item('foo')
print(q.pop())  # Item('grok')

a = Item('foo')
b = Item('bar')
print(a < b)
# Traceback (most recent call last):
#   File "D:/project/CookBook/exercise_0105.py", line 35, in <module>
#     print(a < b)
# TypeError: '<' not supported between instances of 'Item' and 'Item'



# >>> a = (1, 0, Item('foo'))
# >>> b = (5, 1, Item('bar'))
# >>> c = (1, 2, Item('grok'))
# >>> a < b
# True
# >>> a < c
# True
# >>>