from collections import defaultdict

d ={
    'a' : [1, 2, 3],
    'b' : [4, 5]
}
e = {
    'a' : {1, 2 ,3},
    'b' : {4, 5}
}

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
print(d)  # defaultdict(<class 'list'>, {'a': [1, 2], 'b': [4]})

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)
print(d)  # defaultdict(<class 'set'>, {'a': {1, 2}, 'b': {4}})

d = {} # 一个普通的字典
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('b', []).append(4)
print(d)  # defaultdict(<class 'set'>, {'a': {1, 2}, 'b': {4}})

# d ={}
# for key, value in pairs:
#     if key not in d:
#         d[key] = []
#     d[key].append(value)
#
# d = defaultdict(list)
# for key, value in pairs:
#     d[key].append(value)

