from django.test import TestCase
from django.urls import reverse
from myapp.tests import EncryptViewTestCase
from django.contrib.auth.models import User
from myapp.views import encrypt_with_aes256


class EncryptViewTestCase(TestCase):
    def setUp(self):

        self.user = User.objects.create_user(username='test_user', password='test_password')

    def test_encrypt_view(self):

        plaintext = 'I LOVE MTU'
        key = b'i am divine and this is my keyzs' 

        expected_ciphertext = '856315c78d8e8f429c3f56159b6849a1'

        actual_ciphertext = encrypt_with_aes256(plaintext, key)

        self.assertEqual(actual_ciphertext, expected_ciphertext)

    def test_invalid_key(self):

        response = self.client.post(reverse('encrypt_view'), {'plain_text': 'Test plain text', 'key': 'short_key'}, follow=True)

        self.assertEqual(response.status_code, 400)

        self.assertIn('Key must be exactly 32 bytes', response.json().get('error'))
