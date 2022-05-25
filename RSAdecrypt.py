from RSAencrypt import recup

def decrypt():
    """
    It takes the user's choice of whether to decrypt a previously encrypted message or to decrypt an
    external message, and then it decrypts the message using the user's input of d and n
    """
    choice = int(input("\n\nYou want to\n 1 -- Decrypt your previous encryption\n 2 -- Extern encrypted text\n Enter your choice : "))
    if choice == 1:
        encrypt_list, n, d = recup()
        
        decrypt_list = []
        for i in range (len(encrypt_list)):
            decrypt_asc = pow(encrypt_list[i],d,n)
            decrypt_list.append(chr(decrypt_asc))
        print("The encrypted text : ", encrypt_list)
        print("The plain text is : %s" %("".join(decrypt_list)))
    elif choice == 2:
        d = int(input("Enter d : "))
        n = int(input("Enter n : "))
        crypt = input("Message to decrypt : ")
        crypt_list  = crypt.split(" ")
        for k in range (len(crypt_list)):
            crypt_list[k] = int(crypt_list[k])
        decrypt_list = []
        for i in range (len(crypt_list)):
            decrypt_asc = pow(encrypt_list[i],d,n)
            decrypt_list.append(chr(decrypt_asc))
        print("The plain message is : %s" %("".join(decrypt_list)))
    else:
        print("Please select a existing menu")
