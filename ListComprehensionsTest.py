nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Comprehensions and lambda
# my_list = [n for n in nums if n % 2 == 0]
my_list = list(filter(lambda n: n % 2 == 0, nums))
# my_list = list(map(lambda n: n, nums))
print(my_list)
print(2 in nums and 11 in nums)


# Generator
my_gen = (n * n for n in nums)

for n in my_gen:
    print(n)
