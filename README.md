# 🔐 RSA Cryptosystem in Python

This is a clean, simple, and interactive Object-Oriented implementation of the **RSA Cryptosystem** using Python. It allows you to:

- Generate RSA public and private keys
- Encrypt a message using the public key
- Decrypt the ciphertext using the private key
- Understand how RSA works with clear step-by-step console outputs

> **Note:** This tool is meant for educational purposes. It is not optimized for production-level cryptography.

---

## 🚀 Features

- Selectable key sizes: `1024`, `2048`, `3072`, and `4096` bits
- Step-by-step key generation breakdown:
  - Prime generation
  - Modulus `n`, Euler's totient `ϕ(n)`
  - Public exponent `e` and private exponent `d`
- Encrypt and decrypt integer messages
- View full public and private keys
- Clean command-line interface

---

## 🛠️ Requirements

- Python 3.x
- `pycryptodome` library

### Install Dependencies

```bash
pip install pycryptodome
```

---

## 📂 File Structure

```bash
rsa_tool/
├── rsa.py           # Main RSA tool implementation
└── README.md        # Project documentation
```

---

## ⚙️ How to Use

### 1. Run the Script

```bash
python rsa.py
```

### 2. Select RSA Key Size

Choose from 1024, 2048, 3072, or 4096 bits.

### 3. Menu Options

- `1`: Encrypt a Message  
- `2`: Decrypt a Cipher  
- `3`: Show Public/Private Keys  
- `4`: Exit  

---

## 🔑 Example

### Key Generation

```
Key Size Selected: 1024-bit
Generating two large prime numbers p and q...
Step 1: Calculate modulus n = p * q
Step 2: Calculate Euler's Totient Function φ(n)
Step 3: Select public exponent e
Step 4: Compute private exponent d ≡ e⁻¹ mod φ(n)
```

### Encryption

```
Enter message (as a number < n): 123456
Encryption Process:
c = m^e mod n
Ciphertext: c = 789654321...
```

### Decryption

```
Enter ciphertext: 789654321...
Enter private key d: ...
Enter modulus n: ...
Decrypted Message: m = 123456
```

---

## 💡 Educational Objective

This script is built for **learning purposes** to help students and beginners understand:

- How RSA works internally
- The importance of secure key generation
- Why modular arithmetic is core to cryptography

---

## 📌 Disclaimer

This implementation **does not** handle padding, message hashing, or binary data. **Never use this script in real-world cryptographic systems.**

For production-grade cryptography, refer to libraries like:
- [PyCryptodome](https://github.com/Legrandin/pycryptodome)
- [Cryptography](https://cryptography.io/)

---

## 🧑‍💻 Author

**Sujal Adhikari**  
Cybersecurity Enthusiast & Learner  
🔗 [Portfolio](https://sujaladhikari149.com.np)

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
