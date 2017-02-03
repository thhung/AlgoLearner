#!/usr/bin/python

# computing the nth fib number

"""
    ============================================================================
    No memoire =  3.24852895737
    With memoire =  0.0476958751678
    Fastest =  0.0100269317627
    Memoire is faster  68.1092221484  times than no memoire
    Fastest is faster  323.980359521  times than no memoire
    Fastest is faster  4.75677667871  times than memoire
    ============================================================================
    Old Results:
        No memoire =  3.34935688972
        With memoire =  0.0460569858551
        Memoire is faster  72.7220165962  times
    This implementation focuses on the runtime of 1 time you call fib, NOT for
    unit test that you can multiple time of fib. So you will see that, you only
    72 faster than recursive version.
    ============================================================================
"""

class SuperFastFib:
    """
        Focusing on calling fib multiple times.
    """
    def __init__(self):
        self.memoire = [0]*500
    def run(self, n):
        if n == 1 or n == 2:
            self.memoire[n-1] = 1
        else:
            if self.memoire[n-1] == 0:
                self.memoire[n-1] = self.memoire[n-2] + self.memoire[n-3]
        return self.memoire[n-1]



def fib(n):
    """
         Computing the nth of Fib series
         Implemetation focusing on 1 time running of fib.
    """
    memoire = [0] * 100

    def rec_fib(n):
        if n == 1 or n == 2:
            memoire[n-1] = 1
            return 1
        else:
            if memoire[n - 1] == 0:
                memoire[n-1] = memoire[n-1] + memoire[n-2]

                # if you use the line below, the result is less impressive
                # No memoire =  3.22995209694
                # With memoire =  0.156451940536
                # Memoire is faster  20.6450114065  times
                #memoire[n - 1] = rec_fib(n-1) + rec_fib(n-2)
            return memoire[n-1]
    return rec_fib(n)

def fib_no_mm(n):
    if n == 1 or n==2:
        return 1
    else:
        return fib_no_mm(n-1) + fib_no_mm(n-2)

def unit_test1():
    for i in xrange(1,21):
        fib(i)

def unit_test2():
    for i in xrange(1,21):
        fib_no_mm(i)

def unit_test3():
    u = SuperFastFib()
    for i in xrange(1,21):
        u.run(i)


if __name__ == '__main__':
    import timeit
    tmm = timeit.timeit("unit_test1()", setup="from __main__ import unit_test1", number=1000)
    t0mm = timeit.timeit("unit_test2()", setup="from __main__ import unit_test2", number = 1000)
    fastest = timeit.timeit("unit_test3()", setup="from __main__ import unit_test3", number = 1000)
    print "No memoire = ", t0mm
    print "With memoire = ",tmm
    print "Fastest = ", fastest
    print "Memoire is faster ", t0mm/tmm ," times than no memoire"
    print "Fastest is faster ", t0mm/fastest ," times than no memoire"
    print "Fastest is faster ", tmm/fastest ," times than memoire"
