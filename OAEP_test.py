import os
import time
from RSAencrypt import input_text

#base code from https://github.com/mimoo/RSA_PKCS1v1_5_attacks/blob/master/bb98_graphic.sage

start_time = time.time()

def get_byte_length(message):
    res = 0
    if (len(bin(message)) - 2) % 8 != 0:
        res += 1
    res += (len(bin(message)) - 2) // 8
    return res

def padding(message, target_length):
    # 02
    res = 0x02 << 8 * (target_length - 2)
    # random
    random_pad = os.urandom(target_length - 3 - get_byte_length(message))
    for idx, val in enumerate(random_pad):
        res += val << (len(random_pad) - idx + get_byte_length(message)) * 8
    # 00
    # message
    res += message
    print('voici le random pad : ',random_pad)
    return res

def main():
    n =  437272606206591106861256033136078687619825406017895551939289308715919384679348570371423066326364378114460636710288467118094463271193328266791802009992454793778529313737189346175189830057251432454071945039584363725953351445692974496978719262251633450064073744082464850516607530098254921490927535578154127716769
    N_size = get_byte_length(n)
    print(N_size)
    hexplain = []
    list_hex = []
    padded = []
    plain = "test du hexa python"
    for i in range (len(plain)):
        plain_asc = ord(plain[i])
        hexplain.append(plain_asc)
        list_hex.append(hex(hexplain[i]))
    print(list_hex)
    for i in range (len(list_hex)):
        padded.append(padding(hexplain[i], N_size))
    print(padded)


main()
