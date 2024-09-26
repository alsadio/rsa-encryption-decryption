def find_e(p:int, q:int, n:int):
    #calculate (p-1)(q-1)
    a = (p-1) * (q-1)
    e = 0
    for i in range(1, a):
        if (a % i != 0):
            e = i
            break
    return e
def find_d(p:int, q:int, e:int):
    d = 0
    pq_minus = (p-1) * (q-1)
    ed = pq_minus +1
    while ed % e != 0:
        ed += pq_minus
    d = int(ed/e)
    return d
def encrypt(m:int, public_key:tuple):
    e = public_key[0]
    n = public_key[1]

    c = calculate_mod(m, e, n)
    return c

def decrypt(c:int, private_key:tuple):
    d = private_key[0]
    n = private_key[1]

    m = calculate_mod(c, d, n)
    return m
def calculate_mod(num:int, pow:int, mod:int):
    loops = int(pow/2)
    temp_result = 1
    for i in range(loops):
        temp_result *= (num**2) % mod
    if pow % 2 != 0:
        temp_result *= num % mod
    result = temp_result % mod

    return result
if __name__ == '__main__':
    print("Enter the prime numbers, p and q (seperated by space): " , end='')
    p, q = map(int, input().split())
    #product n
    n = p * q
    print(f"p: {p}, q: {q}")

    print("Calculating RSA values ...\n")
    e = find_e(p, q, n)
    d = find_d(p, q, e)   
    RSA_public_key = (e, n)
    RSA_private_key = (d, n)
    print(f"Public RSA key is {RSA_public_key}")
    print(f"Private RSA key is {RSA_private_key}\n")

    m = int(input("Enter the plaintext message m (an integer): "))
    print()
    print("Encrypting m...")
    c = encrypt(m, RSA_public_key)
    print(f"The ciphertext c is {c}\n")

    print("Decrypting c...")
    m = decrypt(c, RSA_private_key)
    print(f"The plaintext m is {m}\n")
