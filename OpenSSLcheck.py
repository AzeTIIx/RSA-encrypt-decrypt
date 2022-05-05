from RSAencrypt import recup_ssl
import math
"""asn1=SEQUENCE:rsa_key

[rsa_key]
version=INTEGER:0
modulus=INTEGER: n
pubExp=INTEGER: e
privExp=INTEGER: d
p=INTEGER: p
q=INTEGER: q
e1=INTEGER: d mod(p-1)
e2=INTEGER: d mod(q-1)
coeff=INTEGER: q^-1 mod p

source : https://stackoverflow.com/questions/19850283/how-to-generate-rsa-keys-using-specific-input-numbers-in-openssl


"""

def gen_int():
    n, d, p, q, e = recup_ssl()
    global e1, e2
    e1 = d %(p-1)
    e2 = d %(q-1)
    return n, d, p, q, e, e1, e2

def findModInverse():
    #source : https://inventwithpython.com/cryptomath.py
    n, d, p, q, e = recup_ssl()
    if math.gcd(q, p) != 1:
            return None # no mod inverse if a & m aren't relatively prime

        # Calculate using the Extended Euclidean Algorithm:
    u1, u2, u3 = 1, 0, q
    v1, v2, v3 = 0, 1, p
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % p


def create_file():
    n, d, p, q, e, e1, e2 = gen_int()
    u1 = findModInverse()
    file = open("mykey.pem", "w")
    file.write("[rsa_key]\n")
    file.write("version=INTEGER:0\n")
    file.write("modulus=INTEGER: %d\n" %n)
    file.write("pubExp=INTEGER: %d\n" %e)
    file.write("privExp=INTEGER: %d\n" %d)
    file.write("p=INTEGER: %d\n" %p)
    file.write("q=INTEGER: %d\n" %q)
    file.write("e1=INTEGER: %d\n" %e1)
    file.write("e2=INTEGER: %d\n" %e2)
    file.write("coeff=INTEGER: %d\n" %u1)
    file.close()

