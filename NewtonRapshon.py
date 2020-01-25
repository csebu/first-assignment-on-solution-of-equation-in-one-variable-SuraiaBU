def func(x):
    return 2*x*x*x-2*x-5


def derivFunc(x):
    return 6*x*x-2

def newtonRaphson(x):
    h = func(x) / derivFunc(x)
    while abs(h) >= 0.0001:
        h = func(x) / derivFunc(x)

        # x(i+1) = x(i) - f(x) / f'(x)
        x = x - h

    print("The value of the root is : ",
          "%.8f" % x)


x0 = 3
newtonRaphson(x0)