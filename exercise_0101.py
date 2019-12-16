p = (4,5)
x, y = p
print(x)  # 4
print(y)  # 5

data = ['ACME', 50, 91.1,(2012,12,21)]
name, shares, price, date = data
print(name)  # ACME
print(date)  # (2012, 12, 21)

name, shares, price, (year, mon, day) = data
print(name)  # ACME
print(year)  # 2012
print(mon)  # 12
print(day)  # 21

# p = (4,5)
# x,y,z = p  #  ValueError: not enough values to unpack (expected 3, got 2)

data =['ACME', 50, 91.1, (2012,12,21)]
_, shares, price, _ = data
print(shares)  # 50
print(price)  # 91.1