from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import base64


def generate_aes_key(password):
    # Derive key dari password menggunakan PBKDF2
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,  # Panjang kunci AES: 256 bit (32 byte)
        salt=b'salt_123',  # Ganti dengan salt yang aman
        iterations=100000,  # Jumlah iterasi PBKDF2
        backend=default_backend()
    )
    key = kdf.derive(password.encode())
    return key


def encrypt_text_aes(text, key):
    # Padding teks agar panjangnya menjadi kelipatan 16 (blok AES)
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(text.encode()) + padder.finalize()

    # Inisialisasi enkripsi dengan kunci dan mode ECB
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    encryptor = cipher.encryptor()

    # Enkripsi teks
    encrypted_text = encryptor.update(padded_data) + encryptor.finalize()

    return base64.b64encode(encrypted_text)


def decrypt_text_aes(encrypted_text, key):
    # Inisialisasi dekripsi dengan kunci dan mode ECB
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    decryptor = cipher.decryptor()

    # Dekripsi teks
    decrypted_padded_data = decryptor.update(encrypted_text) + decryptor.finalize()

    # Hapus padding
    unpadder = padding.PKCS7(128).unpadder()
    unpadded_data = unpadder.update(decrypted_padded_data) + unpadder.finalize()

    return unpadded_data.decode()



if __name__ == '__main__':
    # Buat kunci AES dari password
    password = "istekak"
    aes_key = generate_aes_key(password)

    # Teks yang akan dienkripsi
    text = "Hello, World!"

    # Enkripsi teks
    encrypted_text = encrypt_text_aes(text, aes_key)
    print("Teks yang telah dienkripsi:", encrypted_text)

    # Dekripsi teks
    decrypted_text = decrypt_text_aes(base64.b64decode(encrypted_text), aes_key)
    print("Teks yang telah didekripsi:", decrypted_text)
