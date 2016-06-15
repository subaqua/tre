# Fibonacci numbers module

import sys

def fib(n):
    a, b = 0, 1
    while b < n:
        print b,
        a, b = b, a + b
    print

def fib2(n):
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result

def main(args=sys.argv[1:]):
    if len(args) > 0:
        try:
            n = int(args[0])
        except ValueError:
            print "Not an Integer!"
        else:
            if n > 0:
                print "Fibonaci for argv {} is fib({}) == {}"\
                    .format(args, n, fib2(n)),
            else:
                print "Not a valid integer : {}".format(args)
    else:
        print "usage: fibo <n>"
