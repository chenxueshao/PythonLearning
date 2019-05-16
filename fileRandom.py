# with open('kkk.jpg','rb') as brf:
#     pass


# with open("test.py", "r") as rf:
#     with open("test2.txt", "w") as wf:
#         for line in rf:
#             wf.write(line)

# size_to_read = 10
# f_contents = f.read(size_to_read)

# print(f.tell())

# f.seek(0)
# print(f.tell())

# while len(f_contents) > 0:
#     print(f_contents, end="*")
#     f_contents = f.read(size_to_read)

# for line in f:
#     print(line, end="")

# f_contents = f.readline()
# print(f_contents)

# f = open("test.py", "r")
# f.close()
# print(f.closed)


import random

# r = random.random()
# r = random.uniform(1, 10)
# r = random.randint(3, 100)
greeting = ["hello", "hi", "hei", "howdy", "hola"]
# r = random.choice(greeting)
# r = random.choices(greeting, weights=[18, 18, 2, 2, 10], k=10)

deck = list(range(1, 53))
# random.shuffle(deck)
hand = random.sample(deck, k=5)
print(hand)
