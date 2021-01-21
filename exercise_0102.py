from audioop import avg


def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle)

record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record
print(name)  # Dave
print(email)  # dave@example.com
print(phone_numbers)  # ['773-555-1212', '847-555-1212']
# 值得注意的是上面解压出的 phone_numbers 变量永远都是列表类型，
# 不管解压的电话号码数量是多少（包括 0 个）。
# 所以，任何使用到phone_numbers变量的代码就不需要做多余的类型检查去确认它是否是列表类型了。


# *trailing_qtrs, current_qtr = sales_record
# trailing_avg = sum(trailing_qtrs) / len(trailing_qtrs)
# return avg_comparison(trailing_avg, current_qtr)


*trailing, current = [10, 8, 7, 6, 5, 4, 3, 2, 1]
print(trailing)  # [10, 8, 7, 6, 5, 4, 3, 2]
print(current)  # 1

records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3,4)
]


def do_foo(x,y):
    print('foo', x, y)


def do_bar(s):
    print('bar', s)


for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

line = 'nobady:*:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(uname)  # nobady
print(homedir)  # /var/empty
print(sh)  # /usr/bin/false

record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record
print(name)  # ACME
print(year)  # 2012

items = [1, 10, 7, 4, 5, 9]
head, *tail = items
print(head)  # 1
print(tail)  # [10, 7, 4, 5, 9]


def sum1(items):
    head, *tail = items
    return head + sum1(tail) if tail else head


print(sum1(items))  # 36
