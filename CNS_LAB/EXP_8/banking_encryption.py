
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes

# Original transaction
message = "Transfer Rs.5000 to ABC Bank"

print("Original Message:", message)

# Generate RSA keys
key = RSA.generate(2048)
public_key = key.publickey()
private_key = key

# Generate AES key
aes_key = get_random_bytes(16)

# Encrypt message using AES
aes = AES.new(aes_key, AES.MODE_EAX)
ciphertext, tag = aes.encrypt_and_digest(message.encode())

print("\nEncrypted Message:", ciphertext.hex())

# Encrypt AES key using RSA
rsa = PKCS1_OAEP.new(public_key)
encrypted_key = rsa.encrypt(aes_key)

print("\nAES Key Encrypted Using RSA")

# Decrypt AES key using RSA
rsa = PKCS1_OAEP.new(private_key)
decrypted_key = rsa.decrypt(encrypted_key)

# Decrypt message using AES
aes = AES.new(decrypted_key, AES.MODE_EAX, nonce=aes.nonce)
decrypted_message = aes.decrypt_and_verify(ciphertext, tag)

print("\nDecrypted Message:", decrypted_message.decode())
print("\nTransaction Verified Successfully!")
