class Duck:
    def quack(self):
        print("quack")

    def fly(self):
        print("flap")


class Person:
    def quack(self):
        print("fake quack")

    def fly(self):
        print("fake flap")


def quack_and_fly(thing):
    # # Not Duck-Typed(Non-Pythonic)
    # # if isinstance(thing, Duck):
    #     thing.quack()
    #     thing.fly()
    # else:
    #     print("This has to be a DUCK!")

    # LBYL (Non-Pythonic)
    # if hasattr(thing, "quack"):
    #     if callable(thing.quack):
    #         thing.quack()

    # if hasattr(thing, "fly"):
    #     if callable(thing.fly):
    #         thing.fly()

    # EAFP (Pythonic)
    try:
        thing.quack()
        thing.fly()
        thing.bark()
    except AttributeError as e:
        print(e)

    print()


d = Duck()
quack_and_fly(d)

p = Person()
quack_and_fly(p)

