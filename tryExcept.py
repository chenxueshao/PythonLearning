try:
    # f = open("ddd.txt")
    # f = d
    # f = 1
    raise FileNotFoundError
except FileNotFoundError:
    print("error")
except Exception:
    print("ha")
else:
    print("heh")
finally:
    print("finally")

