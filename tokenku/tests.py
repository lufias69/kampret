from django.test import TestCase

# Create your tests here.

import requests
import base64
from tokenku.tools.enkripsi import generate_aes_key, decrypt_text_aes

# URL API yang ingin diuji
url = 'http://localhost:8000/token/'

# Mengirim permintaan GET ke API
response = requests.get(url)




password = generate_aes_key('istekak')
token = decrypt_text_aes(base64.b64decode(response.json()['data']['token']), password)
print(token)

