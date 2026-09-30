from encrypt import *
from decrypt import *




def ECBencrypt(plaintext, key):
    if len(plaintext) % 8 != 0:
        for i in range(8 - (len(plaintext) % 8)):
            plaintext += "-"
        print(len(plaintext))

    
    final_ciphered_text = ""

    for i in range((len(plaintext) // 8)):
        print("::", plaintext[i * 8: (i+1)*8 ])
        string_block = plaintext[i * 8: min((i+1)*8, len(plaintext)) ]
        ciphered_block  = tandak_beDES_encrypt(string_block, key)
        final_ciphered_text += ciphered_block


    return final_ciphered_text

def ECBdecrypt(cipheredtext, key):
    ln = 16
    final_plain_text = ""

    for i in range(len(cipheredtext) // ln):
        print(":::",cipheredtext[i * ln: (i+1)*ln ])
        string_block = cipheredtext[i * ln: min((i+1)*ln, len(cipheredtext)) ]
        plain_block  = tandak_beDES_decrypt(string_block, key)
        final_plain_text += plain_block


    return final_plain_text


