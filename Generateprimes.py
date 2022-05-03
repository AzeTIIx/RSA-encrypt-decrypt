from RabinMiller import rabin_miller
from RabinMiller import rand
import time

def generate_primes(bits):
    """
    It generates a random number of the specified number of bits, and then tests it to see if it's
    prime. If it's not, it generates another random number and tests it. It keeps doing this until it
    finds a prime number
    :param bits: The number of bits in the prime number
    :return: A prime number
    """

    timestart = time.time()
    while True:
        a = (rand.randrange(1 << bits - 1, 1 << bits) << 1) + 1
        if rabin_miller(a):
            print(f"Prime number found in {time.time() - timestart} seconds")
            return a

