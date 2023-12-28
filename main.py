# תרגיל 1:


# import datetime
#
#
# def myDecorator(func):
#     def wrapper():
#         time1 = datetime.datetime.now().microsecond
#         print(f"time1 = {time1}")
#         func()
#         time2 = datetime.datetime.now().microsecond
#         print(f"time2 = {time2}")
#         time = time2 - time1
#         print(time)
#
#     return wrapper
#
#
# @myDecorator
# def func1():
#     num = 0
#     for i in range(1, 100000000):
#         num += i
#     return
#
#
# if __name__ == '__main__':
#     func1()


# תרגיל 2


def myDecorator(func):
    def wrapper(*args, **kwargs):
        if args[0] in myDictionary:
            result = myDictionary[args[0]]
        else:
            result = func(*args, **kwargs)
            myDictionary.update({args[0]: result})
        print(myDictionary)

        return result

    return wrapper


@myDecorator
def Fibonacci(n):
    fibs = [0, 1]
    for i in range(2, n + 1):
       fibs.append(fibs[-1] + fibs[-2])

    return fibs[n]


if __name__ == '__main__':
    myDictionary = {}
    print(Fibonacci(5))
    print(Fibonacci(4))
    print(Fibonacci(3))
    print(Fibonacci(5))
    print(Fibonacci(4))
    print(Fibonacci(3))
