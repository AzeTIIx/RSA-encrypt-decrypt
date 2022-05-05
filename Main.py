from Generateprimes import generate_primes
from RSAencrypt import outputs
from RSAencrypt import encrypt
from RSAdecrypt import decrypt
import OpenSSLcheck



def home():
    print("\n\n")
    print("------------------------------------------Welcome------------------------------------------\n")
    print(" _____   _____           ______ _   _  _____ _______     _______ _______ _____ ____  _   _\n|  __ \ / ____|  /\     |  ____| \ | |/ ____|  __ \ \   / /  __ \__   __|_   _/ __ \| \ | |\n| |__) | (___   /  \    | |__  |  \| | |    | |__) \ \_/ /| |__) | | |    | || |  | |  \| |\n|  _  / \___ \ / /\ \   |  __| | . ` | |    |  _  / \   / |  ___/  | |    | || |  | | . ` |\n| | \ \ ____) / ____ \  | |____| |\  | |____| | \ \  | |  | |      | |   _| || |__| | |\  |\n|_|  \_\_____/_/    \_\ |______|_| \_|\_____|_|  \_\ |_|  |_|      |_|  |_____\____/|_| \_|\n")
    print("                                                     By Charles AIMIN and Alessandro GADRAT")

def menu():
    #source code from https://computinglearner.com/how-to-create-a-menu-for-a-python-console-application/
    print("\n\n")
    options = {1: 'Generate a random prime number',2: 'Encrypt',3: 'Decrypt',4:'OpenSSl Keygen', 5: 'Exit',}

    def print_menu():
        for key in options.keys():
            print (key, '--', options[key] )

    def option1():
        bits = int(input("You want your number to be what length (bits) : "))
        print(generate_primes(bits))

    def option2():
        outputs()
        encrypt()

    def option3():
        decrypt()

    def option4():
        OpenSSLcheck.create_file()

    if __name__=='__main__':
        while(True):
            print_menu()
            option = ''
            try:
                option = int(input('Enter your choice: '))
            except:
                print('Wrong input. Please enter a number ...')
            if option == 1:
                option1()
            elif option == 2:
                option2()
            elif option == 3:
                option3()
            elif option == 4:
                option4()
            elif option == 5:
                print('Thanks for using our program :)')
                exit()
            else:
                print('Invalid option. Please enter a number between 1 and 4.')

home()
menu()
