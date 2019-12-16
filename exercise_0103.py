from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


# Example use on a file

if __name__ == '__main__':
    with open(r'../cookbook/somefile.txt')as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-' * 20)

q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print(q)  # deque([1, 2, 3], maxlen=3)
q.append(4)
print(q)  # deque([2, 3, 4], maxlen=3)
q.append(5)
print(q)  # deque([3, 4, 5], maxlen=3)


q = deque()
q.append(1)
q.append(2)
q.append(3)
print(q)  # deque([1, 2, 3])
q.appendleft(4)
print(q)  # deque([4, 1, 2, 3])
q.pop()
print(q)  # deque([4, 1, 2])
q.popleft()
print(q)  # deque([1, 2])

