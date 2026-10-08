from essentials_function import *


def generate_all_round_key(C,D, secret_key):
    key_bits = ''.join(format(ord(x), '08b') for x in secret_key)[0:64]
    key_56bits = permute(key_bits, permutated_choice_1_table, 56)
    C, D = key_56bits[:28], key_56bits[28:]

    all_round_key = []
    for i in range(16):
        round_key, C, D = generate_key(C, D, i, key_shifts_amount_table)
        all_round_key.append(round_key)



    return all_round_key

def tandak_beDES_decrypt(secret_text, secret_key):
    key_bits = ''.join(format(ord(x), '08b') for x in secret_key)[0:64]
    key_56bits = permute(key_bits, permutated_choice_1_table, 56)



    cipher_bytes = bytes.fromhex(secret_text)

    secret_bits = ''.join(format(byte, '08b') for byte in cipher_bytes)
    
    intitial_permuted_bits = permute(secret_bits, initial_permutation_table)
    L_split = intitial_permuted_bits[:32]
    R_split = intitial_permuted_bits[32:]


    L_split, R_split = L_split, R_split
    C, D = key_56bits[:28], key_56bits[28:]
    round_keys = generate_all_round_key(C,D, secret_key)
    for round_key in reversed(round_keys):
        L_split, R_split = feistel_round(L_split, R_split, round_key)

    final_swap = R_split + L_split

    plain_bits = permute(final_swap, initial_permutation_table_inverse)

    plain_bytes = int(
        plain_bits,
        2
    ).to_bytes(8, byteorder='big')

    plaintext = plain_bytes.decode('ascii')

    return plaintext

