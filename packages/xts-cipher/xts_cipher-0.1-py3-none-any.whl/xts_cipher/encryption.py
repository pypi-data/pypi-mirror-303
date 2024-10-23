import numpy as np
import random

def generate_keys(num_keys):
    keys = [random.randint(1, 255) for _ in range(num_keys)]
    return keys

def encrypt(message, keys, block_size):
    # Step 1: Substitution
    substituted_text = ''.join([chr((ord(char) + keys[0]) % 256) for char in message])
    
    # Step 2: Transposition
    while len(substituted_text) % block_size != 0:
        substituted_text += ' '  # Padding with spaces if necessary
    transposed_blocks = np.array_split(list(substituted_text), block_size)
    transposed_text = ''.join([char for block in transposed_blocks[::-1] for char in block])
    
    # Step 3: XOR Operation
    for key in keys[1:]:
        transposed_text = ''.join([chr(ord(char) ^ key) for char in transposed_text])
    
    return transposed_text
