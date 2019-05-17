# def squred_nums(nums):
#     for i in nums:
#         yield i * i


# sq = squred_nums([1, 2, 3, 4, 5])
# print(next(sq))
# print(next(sq))
# print(next(sq))
# print(next(sq))
# print(next(sq))
# print(next(sq))

sq = (n * n for n in range(1, 6))
print(list(sq))
for i in sq:
    print(i)


import mem_profile
import random
import time

names = ["john", "ksdkds", "ssd", "dsdsds", "dssd", "ssadd"]
majors = ["sdklk", "dsllkds", "dskl", "wekw", "oewieiwo"]

print(f"Memory (Before): {mem_profile.memory_usage_resource()}Mb")


def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {"id": i, "name": random.choice(names), "major": random.choice(majors)}
        result.append(person)
    return result


def people_generator(num_people):
    for i in range(num_people):
        person = {"id": i, "name": random.choice(names), "major": random.choice(majors)}
        yield person


# t1 = time.clock()
# people = people_list(1000000)
# t2 = time.clock()

t1 = time.clock()
people = people_generator(1000000)
t2 = time.clock()

print(f"Memory (After) : {mem_profile.memory_usage_psutil()}Mb")
print(f"Took {t2-t1} Seconds")

