from encrypt import *
from decrypt import *
from ECB import *

if __name__ == "__main__":
    
    secret_text = "12345678"
    secret_key = "87654321"
    # secret_text = "0123456789ABCDEF"
    # secret_key = "133457799BBCDFF1"
    # if len(secret_key) > 8:
    #     secret_key = secret_key[:8]
    cipher_des = tandak_beDES_encrypt(secret_text, secret_key)
    print(cipher_des)
    dechiper_des = tandak_beDES_decrypt(cipher_des, secret_key)
    # data = bytes.fromhex(dechiper_des)
    # ciphertext_bits = ''.join(format(byte, '08b') for byte in data)
    print(dechiper_des)


    
    a = "123456781234567890"



    


    a = """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris convallis porta turpis sed finibus. Sed non pharetra augue, ac placerat ligula. Curabitur feugiat faucibus tellus a placerat. Praesent maximus est vel lacus tincidunt, ut dignissim justo maximus. Nam vulputate pharetra elementum. Nulla dapibus ac nunc eu bibendum. Etiam eu imperdiet ex. Quisque erat turpis, pulvinar a placerat quis, facilisis at justo. Suspendisse nisl nisl, venenatis vel mauris non, faucibus efficitur nisi.
        Sed viverra ante in mauris cursus venenatis. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nam fermentum lacinia ipsum, et rutrum quam accumsan ac. Duis tempus facilisis dui ac tincidunt. Nullam vestibulum fringilla felis finibus elementum. Pellentesque urna lorem, lobortis ut molestie et, molestie nec nisi. Cras vulputate velit erat, et pharetra leo mollis ac. Suspendisse dignissim consequat tortor ut faucibus. Aliquam congue elementum urna, nec condimentum ligula bibendum eu. Nulla aliquam a enim quis faucibus. In consectetur enim sed elit rhoncus posuere. Aliquam vitae venenatis libero. Quisque posuere orci quis urna euismod venenatis. Nullam interdum elementum magna, at ultricies felis dapibus a. Sed viverra dictum libero et volutpat. Cras ut justo in quam laoreet porttitor.
        Quisque fermentum lacus nec pellentesque imperdiet. Mauris feugiat, tellus eu consequat fringilla, augue lorem facilisis nunc, porta consectetur risus tortor non erat. Nullam maximus id enim ut porta. Pellentesque vulputate, lorem id imperdiet efficitur, sem lacus aliquam dolor, vitae vehicula enim enim id lacus. Donec mattis efficitur placerat. Ut sit amet pellentesque quam. Integer id dolor vitae neque consequat rutrum et ut magna.
        Donec fringilla interdum posuere. Vestibulum vel risus nec arcu aliquet accumsan non et justo. Quisque metus felis, accumsan non sapien vel, malesuada sollicitudin dui. Sed eget auctor mi. Integer volutpat magna lectus, eu tempus purus egestas sed. Morbi convallis magna vel tortor sollicitudin, id efficitur tortor posuere. Praesent ultrices viverra mi, tristique congue odio elementum quis. Ut viverra ut diam commodo pharetra. Donec pulvinar sagittis massa in laoreet. Morbi sit amet turpis eget ante facilisis accumsan sit amet id erat. Proin consequat dui est, eget porttitor risus sagittis eget. Integer ornare metus sed odio ultrices pharetra. Curabitur semper blandit ante vel porta. Nunc non ipsum nec justo pharetra scelerisque eu sed arcu. Proin at risus et dui lobortis convallis.
    """


    a = "Bismillah experimen ku jalan "


    key = "Admin1234"

    encrypted_string = ECBencrypt(a, key)
    print(encrypted_string)


    with open("ciphered_text.txt", "w") as ciphered_file:
        ciphered_file.write(encrypted_string)





    decrypted = ECBdecrypt(encrypted_string,key)
    print(decrypted)
