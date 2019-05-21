class Sentence:
    """Class solution"""

    def __init__(self, sentence):
        self.sentence = sentence
        self.current = self.sentence.strip()

    def __iter__(self):
        return self

    def __next__(self):
        if self.current == "":
            raise StopIteration
        part = self.current.partition(" ")
        self.current = part[2].strip()
        return part[0]


my_sentence = Sentence("This is  a   test")

for word in my_sentence:
    print(word + "*")


def sentence_to_word(sentence):
    """Generator solution"""

    current = sentence.strip()
    while current != "":
        part = current.partition(" ")
        current = part[2].strip()
        yield part[0]


print()
for word in sentence_to_word("this is a test"):
    print(word)
