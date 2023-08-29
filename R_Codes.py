import math

def encrypt(letter, moduli, letter_to_number):
    # Get the number corresponding to the letter
    number = letter_to_number.get(letter, 0)
    print("Number:", number)

    # Calculate the product of all moduli
    N = math.prod(moduli)
    print("N:", N)

    # Calculate the ciphertext for each modulus
    ciphertexts = [(number % n) for n in moduli]
    print("Ciphertexts:", ciphertexts)

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
            return target_letter

    return ""

def decrypt(ciphertext, moduli, letter_to_number):
    # Calculate the product of all moduli
    N = math.prod(moduli)
    print("N:", N)

    # Calculate the modular inverses of each modulus
    inverses = [mod_inverse(N // moduli[i], moduli[i]) for i in range(len(moduli))]
    print("Modular Inverses:", inverses)

    # Calculate the partial decryption for each modulus
    partial_decryptions = [pow(ciphertext, inv, n) for inv, n in zip(inverses, moduli)]
    print("Partial Decryptions:", partial_decryptions)

    # Calculate the Chinese Remainder Theorem solution
    result = sum(partial_decryptions[i] * (N // moduli[i]) for i in range(len(moduli))) % N
    print("Result:", result)

    # Adjust the result to the range 1-26
    adjusted_result = ((result - 1) % 26) + 1

    # Convert the adjusted result back to the corresponding letter
    decrypted_letter = number_to_letter(adjusted_result, letter_to_number)

    return decrypted_letter

# Mapping of alphabet letters to numbers
letter_to_number = {letter: index + 1 for index, letter in enumerate("abcdefghijklmnopqrstuvwxyz")}

# List of pairwise coprime moduli
moduli = [29, 31]

# Letter to encrypt
target_letter = "t"
print("Letter:", target_letter)

# Encryption
ciphertext = encrypt(target_letter, moduli, letter_to_number)
print("Ciphertext:", ciphertext)

# Decryption
decrypted_letter = decrypt(ciphertext, moduli, letter_to_number)
print("Decrypted Letter:", decrypted_letter)

print("Letter to number map:",letter_to_number)
