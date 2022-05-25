from Generateprimes import generate_primes
#from Crypto.Cipher import PKCS1_OAEP #allow me to use padding on my plain text
import math
import random
rand = random.SystemRandom()

def factors():
    """
    It asks the user for a number of bits, then generates two random primes of that length, and returns
    the product of those primes and the totient of that product
    :return: n, phi
    """
    global p, q
    b = int(input("You want your factors n q to be what length (bits) : "))
    """Cette partie sera utile pour avec la fonction -raw car le plaintext doit avoir la même taille (bits) que le produit n.
    text = input("Enter plain text : ")
    a = len(text.encode('utf-8'))
    print(a)
    b = int(a/2)"""
    p = generate_primes(b)
    q = generate_primes(b)
    n = p*q
    print("\n")
    print("We have n = %d \n" %n)
    phi = int((p - 1)*(q - 1))
    print("We have phi(%d) = %d \n" %(n, phi))
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
    print("We have e = %d \n" %e)
    return e

def find_inv(e, phi): #private key d
    """
    It finds the inverse of e mod phi.

    :param e: public key
    :param phi: the totient of n
    :return: The private key d
    """
    #source : https://inventwithpython.com/cryptomath.py
    if math.gcd(e, phi) != 1:
            return None # no mod inverse if a & m aren't relatively prime

        # Calculate using the Extended Euclidean Algorithm:
    d, u2, u3 = 1, 0, e
    v1, v2, v3 = 0, 1, phi
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, d, u2, u3 = (d - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return d % phi

def outputs():
    global e, n, d
    n, phi = factors()
    e = gcd_e(n, phi)
    d = find_inv(e, phi)
    print("We have d = %d \n" %d)
    print("Public key : %d %d \n" %(n,e))
    print("Private key : %d \n" %d)

def input_text():
    """
    It takes a string, converts it to a list, and returns the list.
    :return: A list of the characters in the input string.
    """
    global plain_list, plain
    plain = input("Message to encrypt : ")
    print("\n")
    plain_list  = []
    for k in range (len(plain)):
        plain_list.append(plain[k])
    print("The plain text is :", "".join(plain_list))
    print("\n")
    file = open("message.txt", "w")
    file.write(plain)
    return plain_list, plain

def encrypt():
    """
    It takes the input text, converts it to ASCII, encrypts it, and then converts it to hexadecimal
    :return: the encrypted message, the public key, the modulus, the private key, and the encrypted
    message in hexadecimal.
    """

    global encrypt_list, e, n, d, encrypt_list_hex
    plain_list, plain = input_text()
    encrypt_list = []
    encrypt_list_hex = []
    for i in range (len(plain_list)):
        plain_asc = ord(plain_list[i])
        encrypt_asc = pow(plain_asc,e,n)
        encrypt_list.append(encrypt_asc)
        encrypt_list_hex.append(hex(encrypt_list[i]))
    print("The encrypted message is : ", encrypt_list_hex) #print le cypher text en liste hex pour faire plus h@k3r
    print("\n")

    return encrypt_list, e, n, d, encrypt_list_hex

def recup():
    global encrypt_list, n, d
    return encrypt_list, n, d

def recup_ssl():
    global encrypt_list, n, d, p, q, e, encrypt_list_hex
    return encrypt_list, n, d, p, q, e, encrypt_list_hex




