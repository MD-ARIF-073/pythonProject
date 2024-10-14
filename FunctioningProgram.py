

def make_triple(x):
    return x * 3


my_marks = [10, 20, 30, 40]
result = map(make_triple, my_marks)               # map takes a func and an iterable
print(list(result))