import crypto_functions as cf


def elgamal_demo(p: int, g: int, a: int, r: int, message: int):
    """Demo's encryption and decryption with the given arguments."""

    print("ElGamal")

    # find public key parameter y
    y = g**a % p
    print("Message:", message)
    print("Prime p:", p)
    print("Generator g:", g)
    print("Randomly chosen int r:", r)
    print("Public key parameter y:", y, "\n")

    # keys
    print("Public key y, g, p:", y, g, p)
    print("Private key a:", a, "\n")

    # find k
    k = y**r % p
    print("Parameter k:", k, "\n")

    # encrypt m to find c1 and c2
    c1 = g**r % p
    c2 = message * k % p
    print("Ciphertext c1:", c1)
    print("Ciphertext c2:", c2, "\n")

    # decrypt c1 and c2 to derive k and k1
    d_k = c1**a % p
    k1 = cf.inverse_mod(k, p)
    print("Derived parameter k:", d_k)
    print("Parameter k1:", k1, "\n")

    # decrypt c1 and c2 to verify m
    m = k1 * c2 % p
    print("Decrypted plaintext:", m, "\n")

    return c1, c2, g, a, p, r, y, m


def generate_keys(p: int, g: int, a: int):
    """ Return a dict containing private and public key parameters."""

    y = g**a % p

    return {"p": p, "g": g, "y": y, "a": a}


def sign(g: int, k: int, p: int, a: int, m: int):
    """ Return the signature parameters for a given messsage."""

    r = g**k % p
    k1 = cf.inverse_mod(k, p - 1)
    val = k1 * (m - (a * r))
    s = val % (p - 1)
    return {"r": r, "s": s}


def verify_signature(g: int, y: int, p: int, r: int, s: int, m: int):
    """ Return verification params and boolean result."""

    v = g**m % p
    w = ((y**r) * (r**s)) % p
    return {"result": v == w, "v": v, "w": w}

def homomorphic(ci01, ci02, ci11, ci12, g, a):
    ci21 = ci01 * ci11
    ci22 = ci02 * ci12
    return ci21, ci22


cipher0_1, cipher0_2, g, a, p, r1, y1, m1 = elgamal_demo(23, 2, 5, 7, 8)
cipher1_1, cipher1_2, g, a, p, r2, y2, m2 = elgamal_demo(23, 2, 5, 9, 12)
cipher2_1, cipher2_2 = homomorphic(cipher0_1, cipher0_2, cipher1_1, cipher1_2, g, a)
print('ci1: ', cipher2_1)
print('ci2: ', cipher2_2)

mm = (cipher2_1**(11-a) * cipher2_2) % p
m3 = m1 * m2 % p
print('\n Entschlüsselte multiplizierte Nachricht: ', mm, '\n Original multiplizierte Nachricht: ', m3)

#2 ** 16 % 23 = 9
#2 ** (5 * 16) * 80 % 23 = 19
#9 ** 6 * 19 % 23 = 6