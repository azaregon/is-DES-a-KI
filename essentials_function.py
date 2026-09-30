from tables import *

def permute(bits, table, size = -1):
    if size == -1:
        size = len(table)

    permuted_bits = [0] * size
    
    for i in range(size):
        # #print(i)
        permuted_bits[i] = bits[table[i]-1]


    return ''.join(permuted_bits)



def generate_key(C, D, round, shifts_amount):
    

    rotated_C = C[shifts_amount[round]:] + C[:shifts_amount[round]] # first bit placed at the end
    rotated_D = D[shifts_amount[round]:] + D[:shifts_amount[round]] # first bit placed at the end

    combined = rotated_C + rotated_D
    round_key = permute(combined, permutated_choice_2_table, 48)



    return round_key, rotated_C, rotated_D



def s_box_substitute(bits,s_box_number=1):
    S_Box = S_BOXES[s_box_number-1]
    first_last = bits[0] + bits[5]
    row = int(first_last, 2)
    col = int(bits[1:5], 2)


    converted = S_Box[row][col]
    return format(converted, '04b') # convert back into 4 bits bin


def feistel_round(L_split, R_split,round_key):
    E_expanded_R = permute(R_split, E_expansion_table)
    # E_expanded_L = permute(L_split, E_expansion_table)

    # #print(E_expanded_L, E_expanded_R)

    key_xor_ed = ''.join(str(int(a) ^ int(b)) for a, b in zip(E_expanded_R, round_key))

    #print("E expanded R: ", E_expanded_R)
    #print("XOR with key: ", key_xor_ed)

    s_box_result = ''
    for i in range(len(key_xor_ed) // 6):
        six_bits = key_xor_ed[i*6:(i+1)*6]
        substituted_bits = s_box_substitute(six_bits, s_box_number=i+1)
        s_box_result += substituted_bits
        # #print(f"6 bits: {six_bits} -> Substituted: {substituted_bits}")

    #print(s_box_result)

    feistel_permutation = permute(s_box_result, feistel_p_box)

    final_feistel_xor = ''.join(str(int(a) ^ int(b)) for a, b in zip(feistel_permutation, L_split))

    L_final = R_split
    R_final = final_feistel_xor
    #print("final feistel")
    #print(L_final, R_final)

    return L_final, R_final














