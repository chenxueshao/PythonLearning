# s1 = set([1, 2, 3, 4, 5])
# s1 = set()  # empty set
s1 = {1, 2, 3, 4, 5}
s1.add(6)
s2 = {8, 9, 10, 11}
s1.update([7, 8, 9], s2)
s1.remove(8)
s1.discard(15)
print(s1)
s3 = {1, 3, 5, 7, 9}

s4 = s1.intersection(s2, s3)
s4 = s1.difference(s2)
s4 = s1.difference(s2, s3)
s4 = s1.symmetric_difference(s2)
print(s4)
