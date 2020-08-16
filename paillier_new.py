from random import randint
import time
import libnum
import sys


def gcd(a, b):
    """Compute the greatest common divisor of a and b"""
    while b > 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    """Compute the lowest common multiple of a and b"""
    return a * b // gcd(a, b)


def L(x, n):
    return ((x - 1) // n)


p = 209490258419118348130222483494418126789
q = 177205842835470845473200187961499093143
m = 550304652486555850518304746550

if (len(sys.argv) > 1):
    m = int(sys.argv[1])

if (len(sys.argv) > 2):
    p = int(sys.argv[2])

if (len(sys.argv) > 3):
    q = int(sys.argv[3])

if (p == q):
    print("P and Q cannot be the same")
    sys.exit()

n = p * q

gLambda = lcm(p - 1, q - 1)

g = 37122897808980459097885200962350434983414958591687125308456824153084294507828
#g = randint(20, 150)
if (gcd(g, n * n) == 1):
    print("g is relatively prime to n*n")
else:
    print("WARNING: g is NOT relatively prime to n*n. Will not work!!!")

r = randint(20, 150000)

l = (pow(g, gLambda, n * n) - 1) // n
gMu = libnum.invmod(l, n)

print("\n==Encryption")
start_time = time.time()
k1 = pow(g, m, n * n)
k2 = pow(r, n, n * n)

cipher = (k1 * k2) % (n * n)
print("\nTime to encrypt:", time.time() - start_time, "seconds")

print("\n==Decryption")
start_time = time.time()
l = (pow(cipher, gLambda, n * n) - 1) // n

mess = (l * gMu) % n
print("\nTime to decrypt:", time.time() - start_time, "seconds")

print("p=", p, "\tq=", q)
print("g=", g, "\tr=", r)
print("================")
print("Mu:\t\t", gMu, "\tgLambda:\t", gLambda)
print("================")
print("Public key (n,g):\t\t", n, g)
print("Private key (lambda,mu):\t", gLambda, gMu)
print("================")
print("Message:\t", mess)

print("Cipher:\t\t", cipher)
print("Decrypted:\t", mess)

print("================")
m1 = 22156276073203669139234564254
print("Now we will add a ciphered value of ", m1, " to the encrypted value")


print("\n==Encryption")
start_time = time.time()
k3 = pow(g, m1, n * n)


cipher2 = (k3 * k2) % (n * n)
print("\nTime to encrypt:", time.time() - start_time, "seconds")


ciphertotal = (cipher * cipher2) % (n * n)

print("\n==Decryption")
start_time = time.time()
l = (pow(ciphertotal, gLambda, n * n) - 1) // n

mess2 = (l * gMu) % n
print("\nTime to decrypt:", time.time() - start_time, "seconds")

print("Result:\t\t", mess2)