# f = open("sample.txt", "w")
# f.write("lorem ipsum dolor sit amet, consectetr adipiscing elit.")
# f.close()

# with open('sample.txt', 'w') as f:
#     f.write("lorem ipsum dolor sit amet, consectetr adipiscing elit.")


# class Open_File:
#     def __init__(self, filename, mode):
#         self.filename = filename
#         self.mode = mode

#     def __enter__(self):
#         self.file = open(self.filename, self.mode)
#         return self.file

#     def __exit__(self, exc_type, exc_val, traceback):
#         self.file.close()


# with Open_File("sample.txt", "w") as f:
#     f.write("Testing")

# print(f.closed)


# from contextlib import contextmanager

# @contextmanager
# def open_file(file, mode):
#     f = open(file, mode)
#     yield f
#     f.close()


# with open_file("sample.txt", "w") as f:
#     f.write("lorem ipsum dolor sit amet, consectetr adipiscing elit.")

# print(f.closed)


import os
from contextlib import contextmanager


@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd)


with change_dir("sss"):
    print(os.getcwd())

with change_dir("www"):
    print(os.getcwd())
