from django.shortcuts import render
from django.contrib.auth.hashers import make_password  
from .models import UserProfile, EncryptionKey
from django.http import JsonResponse
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import binascii

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user_password = request.POST.get('password')
        
        # Hash the password before saving it
        hashed_password = make_password(user_password)
        UserProfile.objects.create(email=email, password=hashed_password)
       
    return render(request, 'form.html')


def encrypt_with_aes256(plain_text, key):
    # Pad the plain text to a multiple of AES block size (128 bits or 16 bytes)
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_plain_text = padder.update(plain_text.encode()) + padder.finalize()

    # Create an AES cipher object
    cipher = Cipher(algorithms.AES(key), modes.ECB())
    
    # Encrypt the padded plain text
    encryptor = cipher.encryptor()
    cipher_text = encryptor.update(padded_plain_text) + encryptor.finalize()

    # Encode the cipher text as hexadecimal
    hex_cipher_text = binascii.hexlify(cipher_text).decode()

    return hex_cipher_text



def encrypt_view(request):
    if request.method == 'POST':
        plain_text = request.POST.get('plain_text')
        key = request.POST.get('key')

        if len(key) != 32:
            return JsonResponse({'error': 'Key must be exactly 32 bytes (256 bits) long.'}, status=400)
        
        try:
            # Encode the key as bytes
            key_bytes = key.encode()
            
            # Encrypt the plain text using AES-256 with the provided key
            encrypted_text = encrypt_with_aes256(plain_text, key_bytes)

            # Save the encrypted and the key to the db
            EncryptionKey.objects.create(
            encrypted_text=encrypted_text,
            encryption_key=key,
            user=request.user
        )
            return JsonResponse({'encrypted_text': encrypted_text})
        
        except Exception as e:

            print("Encryption Error:", e)
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return render(request, 'encrypt.html')
    

def decrypt_with_aes256(encrypted_text, key):
   
    # Decode the hexadecimal encoded ciphertext
    cipher_text = binascii.unhexlify(encrypted_text)

    # Create an AES cipher object
    cipher = Cipher(algorithms.AES(key), modes.ECB())  

    # Decrypt the cipher text
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(cipher_text) + decryptor.finalize()

    # Unpad the decrypted data
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    unpadded_data = unpadder.update(decrypted_data) + unpadder.finalize()

    # Decode the bytes to get the plaintext
    plaintext = unpadded_data.decode()

    return plaintext

def decrypt_view(request):
    if request.method == 'POST':
        encrypted_text = request.POST.get('encrypted_text')
        key = request.POST.get('key')

        # Encode the key as bytes
        key_bytes = key.encode()

        # Query the database to check if the key matches the stored encryption key
        encryption_key = EncryptionKey.objects.filter(encryption_key=key).first()

        if not encryption_key:
            return JsonResponse({'error': 'Invalid encryption key'}, status=400)

        # Perform decryption using the provided key
        try:
            decrypted_text = decrypt_with_aes256(encrypted_text, key_bytes)
            return JsonResponse({'decrypted_text': decrypted_text})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return render(request, 'decrypt.html')