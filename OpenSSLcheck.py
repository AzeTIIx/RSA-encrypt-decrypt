from RSAencrypt import recup_ssl
import math
import os

"""
PRIVATE KEY PARAMATERS SYNTHAX :

asn1=SEQUENCE:rsa_key

[rsa_key]
version=INTEGER:0
modulus=INTEGER:n
pubExp=INTEGER:e
privExp=INTEGER:d
p=INTEGER:p
q=INTEGER:q
e1=INTEGER:d mod(p-1)
e2=INTEGER:d mod(q-1)
coeff=INTEGER:q^-1 mod p

source : https://www.rfc-editor.org/rfc/rfc3447#appendix-A.1.2 (chapter A.1.2 RSA private key syntax)


PRIVATE KEY PARAMETERS SYNTHAX :

asn1=SEQUENCE:rsa_key

[rsa_key]
version=INTEGER:0
modulus=INTEGER:n
pubExp=INTEGER:e

source : https://www.rfc-editor.org/rfc/rfc3447#appendix-A.1.2 (chapter A.1.1 RSA public key syntax)

"""

def gen_int():
    """
    fill this part
    :return: n, d, p, q, e, e1, e2
    """
    encrypt_list, n, d, p, q, e,encrypt_list_hex = recup_ssl()
    global e1, e2
    e1 = d %(p-1)
    e2 = d %(q-1)
    return encrypt_list, n, d, p, q, e, e1, e2, encrypt_list_hex

def findModInverse():
    """
    The Extended Euclidean Algorithm is used to find the modular inverse of e (mod (p-1)(q-1))
    :return: The mod inverse of the public key
    """
    #source : https://inventwithpython.com/cryptomath.py
    encrypt_list, n, d, p, q, e, encrypt_list_hex = recup_ssl()
    if math.gcd(q, p) != 1:
            return None # no mod inverse if a & m aren't relatively prime

        # Calculate using the Extended Euclidean Algorithm:
    u1, u2, u3 = 1, 0, q
    v1, v2, v3 = 0, 1, p
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % p


def create_prikey_file():
    """
    It generates a private key file using the openssl command line tool with custom parameters from our program.
    """
    encrypt_list, n, d, p, q, e, e1, e2, encrypt_list_hex = gen_int()
    u1 = findModInverse()
    file = open("prikey_conf.txt", "w")
    file.write("asn1=SEQUENCE:rsa_key\n\n")
    file.write("[rsa_key]\n")
    file.write("version=INTEGER:0\n")
    file.write("modulus=INTEGER:%d\n" %n)
    file.write("pubExp=INTEGER:%d\n" %e)
    file.write("privExp=INTEGER:%d\n" %d)
    file.write("p=INTEGER:%d\n" %p)
    file.write("q=INTEGER:%d\n" %q)
    file.write("e1=INTEGER:%d\n" %e1)
    file.write("e2=INTEGER:%d\n" %e2)
    file.write("coeff=INTEGER:%d\n" %u1)
    file.close()
    os.system("openssl asn1parse -genconf prikey_conf.txt -out prikey.der")
    os.system('openssl rsa -in prikey.der -inform der -text -check > store_pri_key.txt')
    file=open("store_pri_key.txt", "r")
    keylist=[]
    for line in file:
        l=file.readline()
        if l==("RSA key ok\n"):
            while l != "-----END RSA PRIVATE KEY-----\n":
                l=file.readline()
                keylist.append(l)
    privatekey="".join(keylist)
    file.close()
    print(privatekey)
    file=open("prikey.txt", "w")
    file.write(privatekey)
    file.close()
    os.system('mv prikey.txt prikey.pem')



def create_pubkey_file():
    """
    It creates a file called pubkey_conf.txt, which contains the public key information in ASN.1 format.
    
    
    Then, it uses the openssl command line tool to convert the ASN.1 format to a DER format, and then to
    a PEM format. 
    
    The PEM format is the one that we will use to encrypt the message.
    """

    encrypt_list, n, d, p, q, e, e1, e2, encrypt_list_hex = gen_int()
    file = open("pubkey_conf.txt", "w")
    file.write("asn1=SEQUENCE:rsa_key\n\n")
    file.write("[rsa_key]\n")
    file.write("version=INTEGER:0\n")
    file.write("modulus=INTEGER:%d\n" %n)
    file.write("pubExp=INTEGER:%d\n" %e)
    file.close()
    os.system("openssl asn1parse -genconf pubkey_conf.txt -out pubkey.der")
    os.system('openssl rsa -in prikey.pem -outform PEM -pubout -out pubkey.pem')


def crypt_file():
    """
    It creates a file called crypt.txt and writes the encrypted list (by our program) to it.
    """
    encrypt_list, n, d, p, q, e, e1, e2, encrypt_list_hex = gen_int()

    file = open('crypt.txt', 'w')
    file.write("%s" %encrypt_list_hex)
    file.close()

def encrypt_message():
    """
    It encrypts the message.txt file using the public key and stores it in top_secret.enc.
    """
    os.system("openssl rsautl -encrypt -inkey pubkey.pem -pubin -in message.txt -out top_secret.enc") # add -raw
    try:
        with open('top_secret.enc'): pass
    except IOError:
        print("Error : The file cannot be created")
        exit(1)
    print("The encrypted text is : \n")
    os.system("cat top_secret.enc")
    print("\n")

def decrypt_message():
    """
    This function decrypts the message using the private key and outputs the decrypted message
    """
    os.system("openssl rsautl  -decrypt -in top_secret.enc -out plain_out.txt -inkey prikey.pem") # add -raw
    print("The encrypted text is : ")
    os.system("cat plain_out.txt")
    print("\n")
