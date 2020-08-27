import time
from math import gcd

def judge_qr(p,q,n):
    for r in range(1, n):
        if (p-1) % r == 0:
            if gcd(int((p-1)/r), r) == 1 and gcd((q-1), r) == 1:
                #print(y,"quadratic residue =&gt; 0")
                print("mögliche Blocksize r")
                print(r)
    return r
                #return x
            #else:
                #print(y,"quadratic non-residue =&gt; 1")
                #return 1

def encryption(m, r, y, u, n):
    print("\n==Encryption")
    start_time = time.time()
    c = pow(int(y), int(m)) * pow(int(u), int(r)) % n
    print("\nTime to encrypt:", time.time() - start_time, "seconds")
    return c

def decryption(c, p, q, r, y, n):
    print("\n==Decryption")
    start_time = time.time()
    a = pow(c, (int((p-1)*(q-1)/r))) % n
    print(a)
    b = pow(y, (int((p-1)*(q-1)/r))) % n
    print(b)
    i = 0
    while pow(b, i, n) != a:
        i += 1
    print("\nTime to decrypt:", time.time() - start_time, "seconds")
    return i

#def homomorphic():

def main():
    print("Benaloh encryption")
    print("== Key generation")
    #r = input("\tChoose blocksize r: ")
    #r = int(r)
    p = 733
    q = 859
    n = p * q
    #r = judge_qr(p, q, n)
    r = 61
    #r = input("\n\n Choose residue: ")
    #r = 16831
    #print(r)
    #r = int(r)
    y = 51

    print("\t Public key  : ", r, n, y)
    print("\t Private key  : ", p, q)
    m1 = input("\n\n Choose first message: ")
    u = 175884
    enc1 = encryption(m1, r, y, u, n)
    print("\n First Ciphertext: ", enc1)
    dec1 = decryption(enc1, p, q, r, y, n)
    print("\n First Plaintext: ", dec1)

    m2 = input("\n\n Choose second message: ")
    u = 175884
    enc2 = encryption(m2, r, y, u, n)
    print("\n Second Ciphertext: ", enc2)
    dec2 = decryption(enc2, p, q, r, y, n)
    print("\n Second Plaintext: ", dec2)

    mm = int(m1) + int(m2)
    print("\n Plaintext Addition: ", mm)
    enc4 = encryption(mm, r, y, u, n)
    print("\n Ciphertext of Added plains: ", enc4)
    dec4 = decryption(enc4, p, q, r, y, n)
    print("\n Plaintext of Added plains: ", dec4)
    #m1bin = bin(int(m1))
    #m2bin = bin(int(m2))
    #mm = int(m1bin, 2) ^ int(m2bin, 2)
    enc3 = enc1 * enc2
    dec3 = decryption(enc3, p, q, r, y, n)
    print("\n Multiplied Ciphertext: ", enc3)
    print("\n Decrypted Multiplied Ciphertext: ", dec3)


main()
