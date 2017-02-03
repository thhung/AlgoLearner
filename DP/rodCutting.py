#!/usr/bin/python

"""
Definition of problem:
     Given a rod of length n inches and an array of prices that contains prices
     of all pieces of size smaller than n. Determine the maximum value
     obtainable by cutting up the rod and selling the pieces. For example, if
     length of the rod is 8 and the values of different pieces are given as
     following, then the maximum obtainable value is 22 (by cutting in two
     pieces of lengths 2 and 6)

     length   | 1   2   3   4   5   6   7   8
     --------------------------------------------
     price    | 1   5   8   9  10  17  17  20
"""
def solverV1(p,n):
    """
    Args:
        p: the table of the price, p[i] is the price with rod length i
        n: length of given rod.
    return:
        max revenues from sellling cutting rod.
    """
    if n == 0:
        return 0
    q = -1
    for i in xrange(0,n):
        q = max(q,p[i] + solverV1(p, n -1 -i))
    return q

def m_solver2(p,n,r):
    """
        support for top-down approach.
    """
    if r[n-1] >=0:
        return r[n-1]
    q = -1
    if n==0:
        q = 0
    else:
        for i in xrange(1,n+1):
            q = max(q, p[i-1] + m_solver2(p,n-i,r))
    r[n-1] = q
    return q

def solverV2(p,n):
    """
        top-down approach.
        Args:
            same as v1
        return:
            same as v1
    """
    r = [-1] * n
    return m_solver2(p,n,r)
def solverV3(p,n):
    """
        bottom up approach
        infos same as v1
    """
    r = [0]*(n + 1)
    s = [0]*(n + 1)

    for i in xrange(1,n+1):
        q = -1
        for j in xrange(1, i + 1):
            q = max(q, p[j -1] + r[i - j])
        r[i] = q
    return r[n]
def solverv4(p,n):
    """
        In this version, you can print the solution as well
    """
    r = [0]*(n + 1)
    s = [0]*(n + 1) # stores infos about the first pieces

    for i in xrange(1,n+1):
        q = -1
        for j in xrange(1, i + 1):
            if q < p[j -1] + r[i - j]: # this line need to change so we know
                q = p[j -1] + r[i - j] # when to update the q so we know which
                s[i] = j  #pieces we use for optimal solutions
        r[i] = q
    return r,s

def print_solution(p,n):
    r,s = solverv4(p,n)
    sol = []
    while n > 0:
        sol.append(s[n])
        n = n - s[n]
    return ",".join(map(str,sol))

def solver5(p,n,c):
    """
        Modified version of this problem. Now we add that each cut costs c. So
        the revenues = revenues above - cut's costs

        ARGS:
            c : cost for each cut
    """
    r = [0]*(n + 1)
    s = [0]*(n + 1) # stores infos about the first pieces

    for i in xrange(1,n+1):
        q = -1
        for j in xrange(1, i + 1):
            tc = c # that 3 lines mean that if we choose no cut so no cost at
            if j == i: # at all.
                tc = 0
            if q < p[j -1] + r[i - j] - tc: # this line need to change so we know
                q = p[j -1] + r[i - j] - tc# when to update the q so we know which
                s[i] = j  #pieces we use for optimal solutions
        r[i] = q
    return r,s

def print_solutionv2(p,n,c):
    r,s = solver5(p,n,c)
    rev = str(r[n])
    sol = []
    while n > 0:
        sol.append(s[n])
        n = n - s[n]
    return ",".join(map(str,sol)) + "| " + rev

def unit_test1():
    p = [1, 5 , 8  ,9 ,10 , 17,  17 , 20, 24, 30]
    n = 10
    print "Max value of n = ", n, " is ", solverV3(p,n)

def unit_test2():
    p = [1, 5 , 8  ,9 ,10 , 17,  17 , 20, 24, 30]
    n = 10
    print "Max value of n = ", n, " is ", solverV2(p,n)

def unit_test3():
    p = [1, 5 , 8  ,9 ,10 , 17,  17 , 20, 24, 30]
    n = 7
    print "Solution for n = ", n, " is :\n", print_solution(p,n)

def unit_test4():
    p = [1, 5 , 8  ,9 ,10 , 17,  17 , 20, 24, 30]
    n = 7
    c = 1
    print "Solution for n = ", n, " is :\n", print_solutionv2(p,n,c)

if __name__ == '__main__':
    unit_test4()
