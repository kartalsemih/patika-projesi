

x = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]


def flatten(x):
    if len(x) == 0:
        return x
    if isinstance(x[0], list):
        return flatten(x[0]) + flatten(x[1:])
    return x[:1] + flatten(x[1:])

print(flatten([[1,'a',['cat'],2],[[[3]],'dog'],4,5]))

flatten(x)

y = [[1, 2], [3, 4], [5, 6, 7]]

def reverse(y):
   
    y = [[1, 2], [3, 4], [5, 6, 7]]
    y.reverse()
    for i in range(len(y)):
        (y[i])=(y[i])[::-1]

    print(y)

reverse(y)




