
import random
import string
import base64

from essentials_function import *

all_strings = string.ascii_letters + string.digits


def tandak_beDES_encrypt(secret_text, secret_key):

    key_bits = ''.join(format(ord(x), '08b') for x in secret_key)[0:64]
    key_56bits = permute(key_bits, permutated_choice_1_table, 56)

    used_secret_text = secret_text[0:8]#.ljust(64, '0')  # Pad the secret text to 64 characters


    secret_bits = ''.join(format(ord(x), '08b') for x in used_secret_text)[0:64]
    #print(len(secret_bits))
    #print("non permuted bits: ")
    #print(secret_bits)

    intitial_permuted_bits = permute(secret_bits, initial_permutation_table)
    
    #print("permuted bits: ")
    #print(intitial_permuted_bits)

    L_split = intitial_permuted_bits[:32]
    R_split = intitial_permuted_bits[32:]

    #print(L_split, R_split)
    #print()
    #print()
    #print()

    ## Feistel round

    L_split, R_split = L_split, R_split
    C, D = key_56bits[:28], key_56bits[28:]
    for i in range(16):
        round_key, C, D = generate_key(C, D, i, key_shifts_amount_table)
        L_split, R_split = feistel_round(L_split, R_split, round_key)


    final_swap = R_split + L_split
    final_permuted_bits = permute(final_swap, initial_permutation_table_inverse)

    #print(f"final permuted bits: {final_permuted_bits}")
    #print(f"final len permuted bits: {len(final_permuted_bits)}")


    data = int(final_permuted_bits, 2).to_bytes(8, byteorder='big')

    asB16 = data.hex().upper()

    return asB16



