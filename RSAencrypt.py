from Generateprimes import generate_primes
import math
import time
import random
rand = random.SystemRandom()


def factors():
    """
    It asks the user for a number of bits, then generates two random primes of that length, and returns
    the product of those primes and the totient of that product
    :return: phi, n
    """
    b = int(input("You want your factors n q to be what length (bits) : "))
    p = generate_primes(b)
    q = generate_primes(b)
    n = p*q
    print("We have n = ", n)
    phi = int((p - 1)*(q - 1))
    print("We have phi(%d) = %d " %(n, phi))
    return n, phi

def gcd_e(n, phi): #totient of n
    """
    It generates a random number between 1 and n, and then checks if it is coprime with phi. If it is,
    it returns the number. If it isn't, it generates another random number and checks again
    :param n: the modulus
    :param phi: the totient of n
    :param e: the public key
    :return: The value of e.
    """
    while True:
        e = rand.randrange(1, n)
        gcd = int(math.gcd(e, phi))
        if gcd == 1:
            break
    print("We have e = ",e)
    return e

def find_inv(e, phi): #private key d
    """
    It finds the inverse of e mod phi.

    :param e: public key
    :param phi: the totient of n
    :return: The private key d
    """
    timestart = time.time()
    for d in range(1,phi):
        if((e%phi)*(d%phi) % phi==1):
            print(f"We have d = %d found in {time.time() - timestart} seconds" %d)
            return d


def outputs():
    global e, n, d
    n, phi = factors()
    e = gcd_e(n, phi)
    d = find_inv(e, phi)
    print("Public key : ", n, e)
    print("Private key : ", d)


def input_text():
    """
    It takes a string, converts it to a list, and returns the list.
    :return: A list of the characters in the input string.
    """
    plain = input("Message to encrypt : ")
    plain_list  = []
    for k in range (len(plain)):
        plain_list.append(plain[k])
    print("The plain text is :", "".join(plain_list))
    return plain_list

def encrypt():
    """
    It takes a list of characters, converts them to ASCII, encrypts them, and then converts them back to
    encrypted characters.
    """
    global encrypt_list, e, n, d
    plain_list = input_text()
    encrypt_list = []
    for i in range (len(plain_list)):
        plain_asc = ord(plain_list[i])
        encrypt_asc = (plain_asc**e)%n
        encrypt_list.append(encrypt_asc)
    print("The encrypted message is : ", encrypt_list)
    return encrypt_list, e, n, d

def recup():
    global encrypt_list, n, d
    return encrypt_list, n, d





