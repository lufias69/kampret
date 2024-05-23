import os
import django

from getToken import ApiManager
import enkripsi as enk
import base64


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kampret.settings')
django.setup()

from tokenku.models import WsFeeder

# Mengambil data dengan ID=1
# try:
#     ws_feeder = WsFeeder.objects.get(id=1)
#     # Lakukan sesuatu dengan data yang diambil
#     print("Data yang ditemukan:")
#     print("URL:", ws_feeder.url)
#     print("Username:", ws_feeder.username)
#     print("Password:", ws_feeder.password)
# except WsFeeder.DoesNotExist:
#     print("Data dengan ID=1 tidak ditemukan.")

ws_feeder = WsFeeder.objects.get(id=1)
api_manager = ApiManager(api_url=ws_feeder.url, username=ws_feeder.username, password=ws_feeder.password)
token_response = api_manager.get_token()
token = token_response['data']['token']
# print(token)

password = "istekak"
aes_key = enk.generate_aes_key(password)

# Teks yang akan dienkripsi
# text = "Hello, World!"

# Enkripsi teks
encrypted_text = enk.encrypt_text_aes(token, aes_key)
print("Teks yang telah dienkripsi:", encrypted_text)

# Dekripsi teks
decrypted_text = enk.decrypt_text_aes(base64.b64decode(encrypted_text), aes_key)
print("Teks yang telah didekripsi:", decrypted_text)


token_response['data']['token'] = encrypted_text

print(token_response)

