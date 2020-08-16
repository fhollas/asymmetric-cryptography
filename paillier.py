import crypto_functions as cf
import time
from math import gcd


def paillier_demo(p: int, q: int, m: int, g: int, r: int):
    """Dems encryption and decryption with the given arguments."""

    print("Paillier")

    # find public key param n
    n = p * q
    print("Message m:", m)
    print("Primes p & q:", p, q)
    print("Public key parameter n:", n)
    print("Public key parameter g:", g)

    # find private key params (ƛ, μ)
    ƛ = cf.lcm(p - 1, q - 1)
    k = cf.L((g**ƛ) % (n**2), n)
    μ = cf.inverse_mod(k, n)
    print("Private key parameter ƛ:", ƛ)
    print("Pre-parameter k:", k)
    print("Private key parameter μ:", μ, "\n")

    # keys
    print("Public key (n, g):", n, g)
    print("Private key (ƛ, μ):", ƛ, μ, "\n")

    # find ciphertext c = g**m r**n mod n**2
    c = pow(g, m) * pow(r, n) % pow(n, 2)
    print("Ciphertext:", c)

    # decrpyt c to verify the plaintext m
    p = cf.L(pow(c, ƛ) pow(n, 2), n) * μ % n
    print("Decrypted plaintext:", p)

    return c


def generate_keys(p: int, q: int, g: int):
    """ Return a dict containing private and public key parameters."""

    n = p * q
    ƛ = cf.lcm(p - 1, q - 1)
    k = cf.L((g**ƛ) % (n**2), n)
    μ = cf.inverse_mod(k, n)

    return {"n": n, "g": g, "ƛ": ƛ, "μ": μ}


def encrypt(n: int, g: int, r: int, m: int):
    """ Return encrypted ciphertext."""

    return g**m * r**n % n**2


def decrypt(ƛ: int, μ: int, n: int, c: int):
    """ Return decrypted plaintext."""

    return cf.L(c**ƛ % n**2, n) * μ % n

cipher1 = paillier_demo(733, 859, 53, , 17)
