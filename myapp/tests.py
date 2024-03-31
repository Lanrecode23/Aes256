from django.test import TestCase
from .views import encrypt_with_aes256, decrypt_with_aes256

class EncryptionDecryptionTests(TestCase):

    def test_encryption_decryption(self):
        plain_text = "I LOVE MTU"
        key = b"i am divine and this is my keyzs" 

        encrypted_text = encrypt_with_aes256(plain_text, key)
        decrypted_text = decrypt_with_aes256(encrypted_text, key)

        self.assertEqual(plain_text, decrypted_text)

