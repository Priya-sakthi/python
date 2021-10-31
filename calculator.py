import operator
W = input('Please enter a string ')
def most_frequent(string):
    d = dict()
    for key in string:
        if key not in d:
             d[key] = 1
        else:
            d[key] += 1
    return d
v=print(most_frequent(W))
