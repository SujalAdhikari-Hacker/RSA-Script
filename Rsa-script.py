from Crypto.Util.number import getPrime, inverse, GCD
import sys

class RSA:
    def __init__(self, bit_size):
        self.bit_size = bit_size
        self.p = None
        self.q = None
        self.n = None
        self.phi = None
        self.e = None
        self.d = None
        self.generate_keys()

    def generate_keys(self):
        print(f"\nKey Size Selected: {self.bit_size}-bit")
        print("Generating two large prime numbers p and q...")
        self.p = getPrime(self.bit_size // 2)
        self.q = getPrime(self.bit_size // 2)
        while self.p == self.q:
            self.q = getPrime(self.bit_size // 2)

        print(f"p = {self.p}")
        print(f"q = {self.q}")

        self.n = self.p * self.q
        print(f"\nStep 1: Calculate modulus n = p * q")
        print(f"        n = {self.p} * {self.q} = {self.n}")

        self.phi = (self.p - 1) * (self.q - 1)
        print(f"\nStep 2: Calculate Euler's Totient Function ϕ(n) = (p - 1)(q - 1)")
        print(f"        ϕ(n) = ({self.p - 1}) * ({self.q - 1}) = {self.phi}")

        self.e = 65537
        if GCD(self.e, self.phi) != 1:
            print("Default e = 65537 is not coprime with ϕ(n), finding another valid e...")
            self.e = 3
            while GCD(self.e, self.phi) != 1:
                self.e += 2

        print(f"\nStep 3: Select public exponent e such that gcd(e, ϕ(n)) = 1")
        print(f"        e = {self.e}")

        self.d = inverse(self.e, self.phi)
        print(f"\nStep 4: Compute private exponent d ≡ e⁻¹ mod ϕ(n)")
        print(f"        d = {self.d}")

    def encrypt(self, m):
        print("\nEncryption Process:")
        print("Public Key (e, n):")
        print(f"e = {self.e}")
        print(f"n = {self.n}")
        print(f"\nc = m^e mod n")
        print(f"c = {m}^{self.e} mod {self.n}")
        c = pow(m, self.e, self.n)
        print(f"Ciphertext: c = {c}")
        return c

    def decrypt(self, c, d, n):
        print("\nDecryption Process:")
        print("Private Key (d, n):")
        print(f"d = {d}")
        print(f"n = {n}")
        print(f"\nm = c^d mod n")
        print(f"m = {c}^{d} mod {n}")
        m = pow(c, d, n)
        print(f"Decrypted Message: m = {m}")
        return m

    def show_keys(self):
        print("\nPublic Key:")
        print(f"e = {self.e}")
        print(f"n = {self.n}")
        print("\nPrivate Key:")
        print(f"d = {self.d}")
        print(f"n = {self.n}")
        print(f"ϕ(n) = {self.phi}")
        print(f"Bit Length of n: {self.n.bit_length()} bits")

def main():
    print("\n" + "=" * 60)
    print("              RSA Cryptosystem: Python Tool")
    print("=" * 60)

    print("Choose RSA Key Size:")
    print("1. 1024-bit")
    print("2. 2048-bit")
    print("3. 3072-bit")
    print("4. 4096-bit")

    bit_map = {'1': 1024, '2': 2048, '3': 3072, '4': 4096}
    choice = input("Enter choice (1-4): ").strip()
    bit_size = bit_map.get(choice)

    if not bit_size:
        print("Invalid choice. Exiting.")
        sys.exit(1)

    rsa = RSA(bit_size)

    while True:
        print("\n===== RSA MENU =====")
        print("1. Encrypt a Message")
        print("2. Decrypt a Cipher")
        print("3. Show Public/Private Keys")
        print("4. Exit")
        print("====================")
        ch = input("Enter option: ").strip()

        if ch == '1':
            try:
                m = int(input("Enter message (as a number < n): "))
                if m >= rsa.n:
                    print("Message must be less than n.")
                else:
                    rsa.encrypt(m)
                    print("\nPrivate Key (d, n):")
                    print(f"d = {rsa.d}")
                    print(f"n = {rsa.n}")
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif ch == '2':
            try:
                c = int(input("Enter ciphertext (numeric): "))
                d = int(input("Enter private key d: "))
                n = int(input("Enter modulus n: "))
                rsa.decrypt(c, d, n)
            except ValueError:
                print("Invalid input. Please enter valid numeric values.")

        elif ch == '3':
            rsa.show_keys()

        elif ch == '4':
            print("Exiting.")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
