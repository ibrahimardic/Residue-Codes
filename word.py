import math

def encrypt(number, moduli):
    # Calculate the product of all moduli
    N = math.prod(moduli)

    # Calculate the ciphertext for each modulus
    ciphertexts = [(number % n) for n in moduli]

    # Calculate the Chinese Remainder Theorem solution
    result = sum(ciphertexts[i] * (N // moduli[i]) * mod_inverse(N // moduli[i], moduli[i]) for i in range(len(moduli)))

    # Return the result modulo N
    return result % N

def mod_inverse(a, m):
    # Calculate the modular inverse of a modulo m using Extended Euclidean Algorithm
    if math.gcd(a, m) != 1:
        raise ValueError("The modular inverse does not exist.")

    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m

    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (
            (u1 - q * v1),
            (u2 - q * v2),
            (u3 - q * v3),
            v1,
            v2,
            v3,
        )

    return u1 % m

def number_to_letter(number, letter_to_number):
    # Convert a number back to the corresponding letter
    for letter, value in letter_to_number.items():
        if value == number:
            return letter

    return ""

def decrypt(ciphertext, moduli, letter_to_number):
    # Calculate the product of all moduli
    N = math.prod(moduli)

    # Calculate the modular inverses of each modulus
    inverses = [mod_inverse(N // n, n) for n in moduli]

    # Calculate the partial decryption for each modulus
    partial_decryptions = [pow(ciphertext, inv, n) for inv, n in zip(inverses, moduli)]
    print("Partial decryptions:", partial_decryptions)

    # Calculate the Chinese Remainder Theorem solution
    result = sum(partial_decryptions[i] * (N // moduli[i]) for i in range(len(moduli))) % N
    print("Result:", result)

    # Retrieve the letters corresponding to the numbers
    decrypted_text = ""

    for number in partial_decryptions:
        letter = number_to_letter(number - 1, letter_to_number)  # Subtract 1 to map it back to letters correctly
        if letter:
            decrypted_text += letter

    return decrypted_text

# Mapping of alphabet letters to numbers
letter_to_number = {letter: index + 1 for index, letter in enumerate("abcdefghijklmnopqrstuvwxyz")}
# print("Letter to number mapping:", letter_to_number)

# List of pairwise coprime moduli
moduli = [29, 31, 37, 41, 43, 47, 53, 59, 61, 67]
print("Moduli:", moduli)

# Phrase to encrypt
plaintext = "cryptology"
print("Plaintext:", plaintext)

# Encryption
encrypted_number = sum(letter_to_number.get(c, 0) for c in plaintext)
print("Encrypted number:", encrypted_number)
ciphertext = encrypt(encrypted_number, moduli)
print("Ciphertext:", ciphertext)

# Decryption
decrypted_text = decrypt(ciphertext, moduli, letter_to_number)
print("Decrypted:", decrypted_text)
