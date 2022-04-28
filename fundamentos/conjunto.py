a = {1, 2, 3}
print(type(a))
a = set('cod3r')
print(a)
print('3' in a, 3 not in a)
print({1, 2, 3} == {3, 2, 1, 3})

# operacoes
c1 = {1, 2}
c2 = {2, 3}
print(c1.union(c2))
print(c1.intersection(c2))
c1.update(c2)
print(c1)
print(c2 <= c1)
print(c2 >= c1)
print({1, 2, 3} - {2})
print(c1 - c2)
c1 -= c2
print(c1)
