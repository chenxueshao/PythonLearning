import itertools
import operator

# counter = itertools.count(start=5, step=5)

# print(next(counter))
# print(next(counter))
# print(next(counter))

# data = [22, 3, 33, 4, 5]
# daily_data = list(itertools.zip_longest(range(10), data))
# print(daily_data)

# counter = itertools.cycle([1, 2, 3])

# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))

# counter = itertools.repeat([1, 2, 3], times=3)
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))

# squares = map(pow, range(10), itertools.repeat(2))
# print(list(squares))


# squares = itertools.starmap(pow, [(1, 2), (2, 2), (3, 2), (8, 2)])
# print(list(squares))


letters = ["a", "b", "c", "d"]
numbers = [0, 1, 2, 3, 2, 1, 0]
names = ["Corey", "Nicole"]

# result = itertools.combinations(letters, 2)
# result = itertools.permutations(letters, 2)
# result = itertools.product(numbers, names, repeat=2)
# result = itertools.combinations_with_replacement(numbers, 3)

# for item in result:
#     print(item)

# combined = itertools.chain(letters, numbers, names)

# result = itertools.islice(range(10), 2, 8, 2)

# for item in result:
#     print(item)

selectors = [True, True, False, True]

# result = itertools.compress(letters, selectors)


def lt_2(n):
    return True if n < 2 else False


# result = filter(lt_2, numbers)
# result = itertools.filterfalse(lt_2, numbers)
# result = itertools.dropwhile(lt_2, numbers)
# result = itertools.takewhile(lt_2, numbers)

# result = itertools.accumulate(numbers)
result = itertools.accumulate(numbers, operator.mul)


for item in result:
    print(item)

# itertools.groupby()

copy1, copy2 = itertools.tee(result)
