import time
from math import gcd

def judge_qr(r,p,q):
    if gcd(int((p-1)/r), r) == 1 and gcd((q-1), r) == 1:
        #print(y,"quadratic residue =&gt; 0")
        return 0
    else:
        #print(y,"quadratic non-residue =&gt; 1")
        return 1

def encryption(m, r, y, u, n):
    c = int(y)**int(m) * int(u)**int(r) % n
    return c

def decryption(c, p, q, r, y, n):
    a = c**(int((p-1)*(q-1)/r)) % n
    print(a)
    b = y**(int((p-1)*(q-1)/r)) % n
    print(b)
    i = 0
    while b**i % n != a:
        i += 1
    return i

#def homomorphic():

def main():
    print("Benaloh encryption")
    print("== Key generation")
    r = input("\tChoose blocksize r: ")
    r = int(r)
    p = 103844424493729464783673436514325107389112184776492347900099959731614955567490392579564120780857291112347896056456188129582564961133333856416387132749066549899710337780162622292600478431747771806899068919131433458433085882570972536194784150618125321731296810296832511691166687368982763828142123821022680691339
    q = 160283770205384345997533038230645880268166974777038928584444206535124606514435532145858726210499376660618434101461226634649209980625348422871851049431800339811789806684434471096776552249689143478749442935655840910669488237008060175191695379212241652870850887940832465755491637648303890655926513564059082298849
    n = p * q
    valid = judge_qr(r, p, q)
    y = 85147

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
    enc4 = encryption(mm, r, y, u, n)
    print("\n Ciphertext of Added plains: ", enc4)
    dec4 = decryption(enc4, p, q, r, y, n)
    print("\n Plaintext of Added plains: ", dec4)
    #m1bin = bin(int(m1))
    #m2bin = bin(int(m2))
    #mm = int(m1bin, 2) ^ int(m2bin, 2)
    print("\n Plaintext Addition: ", mm)
    enc3 = enc1 * enc2
    dec3 = decryption(enc3, p, q, r, y, n)
    print("\n Multiplied Ciphertext: ", enc3)
    print("\n Multiplied Plaintext: ", dec3)


main()
