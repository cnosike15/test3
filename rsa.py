#tqe8fn@virginia.edu
# Nneoma Nosike

import random
from math import gcd

from sympy import isprime, mod_inverse

#getting random prime numbers from 2 to 1000000
def generate_prime():
    while True:
        randValue = random.randint(2, 1000000)
        if isprime(randValue):
            return randValue

#function for encryption
def rsa_encrypt(unicode_values, e, n):
    encrypted_values = [pow(char, e, n) for char in unicode_values]
    return encrypted_values
#my input
message = input("Enter message: ")

# Convert the phrase to ASCII values and concatenate them
unicode_values = [ord(char) for char in message]

#function for decryption
def rsa_decrypt(ciphertext, d, n):
    decrypted_values = [pow(char, d, n) for char in ciphertext]
    return decrypted_values

#generating random p and q from calling function
p = generate_prime()
q = generate_prime()

#RSA math
n = p * q
phi_n = (p - 1) * (q - 1)

e = 2


#getting e
while (e < phi_n) and gcd(e, phi_n) != 1:
	e+=1


#getting d
d = pow(e,-1, phi_n)


ciphertext = rsa_encrypt(unicode_values, e, n)

decrypted_message = rsa_decrypt(ciphertext, d, n)

#this is printing out the p, q, private key, public key, ciphertext, and encrypted/decrypted message
print("p:", p)
print("q:", q)
print("e:", e)
print("d:", d)
print("Encrypted message:", ciphertext)
print("Decrypted message:", "".join(chr(char) for char in decrypted_message))



