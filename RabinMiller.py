import random
rand = random.SystemRandom() #cryptographically safe random number

def prime_test(n, a):
    """
    It returns True if n is prime, and False if n is composite
    :param n: the number to be tested
    :param a: the number to be tested
    :return: True or False
    """
    x = n - 1
    while not x & 1:
        x >>=1
    if pow(a, x, n) == 1:
        return True
    while x < n - 1:
        if pow(a, x, n) == n - 1:
            return True
        x <<= 1
    return False

def rabin_miller(n, k = 80):
    """
    If the number passes the Miller-Rabin test k times, then it's probably prime
    :param n: the number to be tested
    :param k: the number of times to run the test, defaults to 80 (optional)
    :return: True or False
    """
    for i in range(k):
        a = rand.randrange(2, n - 1)
        if not prime_test(n, a):
            return False
    return True



