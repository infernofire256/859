from hashlib import *

def hash_loop(message, hash_itr):
    for i in range(hash_itr):
        message=sha512(message.encode()).hexdigest()

print("SHA-512:",hash_loop("test", 1))