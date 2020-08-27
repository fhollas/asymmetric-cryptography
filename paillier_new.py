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


p = 103844424493729464783673436514325107389112184776492347900099959731614955567490392579564120780857291112347896056456188129582564961133333856416387132749066549899710337780162622292600478431747771806899068919131433458433085882570972536194784150618125321731296810296832511691166687368982763828142123821022680691339
q = 160283770205384345997533038230645880268166974777038928584444206535124606514435532145858726210499376660618434101461226634649209980625348422871851049431800339811789806684434471096776552249689143478749442935655840910669488237008060175191695379212241652870850887940832465755491637648303890655926513564059082298849
m = 1145863482667666809174044908307
m1 = 57081308969036885647762169991

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
print("Time to encrypt:", time.time() - start_time, "seconds")

print("\n==Decryption")
start_time = time.time()
l = (pow(cipher, gLambda, n * n) - 1) // n

mess = (l * gMu) % n
print("Time to decrypt:", time.time() - start_time, "seconds")

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
print("Now we will add a ciphered value of ", m1, " to the encrypted value")


print("\n==Encryption 2")
start_time = time.time()
k3 = pow(g, m1, n * n)


cipher2 = (k3 * k2) % (n * n)
print("Time to encrypt:", time.time() - start_time, "seconds")

print("\n==Decryption 2")
start_time = time.time()
l = (pow(cipher2, gLambda, n * n) - 1) // n

mess3 = (l * gMu) % n
print("Time to decrypt:", time.time() - start_time, "seconds")
print(mess3)

print("\n==Add ciphers:")
start_time = time.time()
ciphertotal = (cipher * cipher2) % (n * n)
print("Time to add ciphers:", time.time() - start_time, "seconds")
print("added cipher:", ciphertotal)

print("\n==Decryption")
start_time = time.time()
l = (pow(ciphertotal, gLambda, n * n) - 1) // n

mess2 = (l * gMu) % n
print("Time to decrypt:", time.time() - start_time, "seconds")

print("Result:\t\t", mess2)
