import numpy as np

def decrypt(encrypted_message, keys, block_size):
    # Step 1: Reverse XOR
    for key in reversed(keys[1:]):
        encrypted_message = ''.join([chr(ord(char) ^ key) for char in encrypted_message])
    
    # Step 2: Reverse Transposition
    transposed_blocks = np.array_split(list(encrypted_message), block_size)
    transposed_back = ''.join([char for block in transposed_blocks[::-1] for char in block])
    
    # Step 3: Reverse Substitution
    decrypted_text = ''.join([chr((ord(char) - keys[0]) % 256) for char in transposed_back])
    
    return decrypted_text
