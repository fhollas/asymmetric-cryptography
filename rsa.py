import crypto_functions as cf
import time

def rsa_demo(p: int, q: int, e: int, message: int):
    """Demo's encryption and decryption with the given arguments."""
    print("RSA")

    # find public key param n
    n = p * q
    print("Message:", message)
    print("Primes p & q:", p, q)
    print("Public key parameter n: ", n)
    print("Public key parameter e: ", e)

    # find phi(n) and private key parameter d
    phi_n = (p - 1) * (q - 1)
    d = cf.inverse_mod(e, phi_n)
    print("Phi(n):", phi_n)
    print("Private key parameter d:", d, "\n")

    # keys
    print("Public key n, e:", n, e)
    print("Private key n, d:", n, d)

    # create ciphetext c = m**e % n
    print("\n==Encryption")
    start_time = time.time()
    c = pow(message, e, n)
    print("\nTime to encrypt:", time.time() - start_time, "seconds")
    print("Ciphertext:", c)

    # decrypt c to verify plaintext m
    print("\n==Decryption")
    start_time = time.time()
    m = pow(c, d, n)
    print("\nTime to decrypt:", time.time() - start_time, "seconds")
    print("Decrypted plaintext:", m)

    return c


def generate_keys(p: int, q: int, e: int):
    """ Return a dict containing private and public key parameters."""

    n = p * q
    d = cf.inverse_mod(e, (p - 1) * (q - 1))
    phi_n = (p - 1) * (q - 1)

    return {"n": n, "e": e, "d": d, "phi_n": phi_n}


def encrypt(n: int, e: int, m: int):
    """ Return encrypted ciphertext."""
    ciphertext = m**e % n
    return ciphertext


def decrypt(n: int, d: int, c: int):
    """ Return decrypted plaintext."""

    return c**d % n


def sign(n: int, d: int, m: int):
    """ Return the signature for a given messsage."""

    return m**d % n


def verify_signature(n: int, e: int, s: int, m: int):
    """ Return true if signature matches message."""

    v = s**e % n
    print("Verfied m:", v)
    return v == m

def homomorphic(ci1, ci2, e, d):
    print("\n==Multiplication")
    start_time = time.time()
    ci3 = ci1 * ci2
    print("\nTime to multiply:", time.time() - start_time, "seconds")
    print('\nMultiplied cipher: ', ci3)
    print("\n==Decrypt multiplied cipher")
    start_time = time.time()
    dec3 = pow(ci3, d, n)
    print("\nTime to decrypt:", time.time() - start_time, "seconds")
    return dec3


#cipher1 = rsa_demo(7, 9, 5, int('110011', 2))
cipher1 = rsa_demo(209490258419118348130222483494418126789, 177205842835470845473200187961499093143, 320697230375185983296943967089956439199, 550304652486555850518304746550)
print('\n Cipher 1:', cipher1)
#cipher2 = rsa_demo(7, 9, 5, int('110101', 2))
cipher2 = rsa_demo(209490258419118348130222483494418126789, 177205842835470845473200187961499093143, 320697230375185983296943967089956439199, 22156276073203669139234564254)
print('\n Cipher 2:', cipher2)
cipher3 = rsa_demo(209490258419118348130222483494418126789, 177205842835470845473200187961499093143, 320697230375185983296943967089956439199, 12192701804860537419905592943941808347725613386669159823700)
print('\n Cipher 3:', cipher3)
p = 209490258419118348130222483494418126789
q = 177205842835470845473200187961499093143
n = p * q
phi_n = (p - 1) * (q - 1)
e = 320697230375185983296943967089956439199
d = cf.inverse_mod(e, phi_n)
dec = homomorphic(cipher1, cipher2, e, d)
print('\n Decryption 3:', dec)