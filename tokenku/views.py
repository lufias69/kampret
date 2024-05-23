from django.http import JsonResponse
from django.shortcuts import render
from requests import request

from rest_framework import viewsets
from .models import WsFeeder
from .serializers import WsFeederSerializer

# class token(viewsets.ModelViewSet):
#     queryset = WsFeeder.objects.all()
#     # print(queryset)
#     serializer_class = WsFeederSerializer


import os
import django

from tokenku.tools.getToken import ApiManager
import tokenku.tools.enkripsi as enk
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


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class TokenView(APIView):
    def get(self, request):
        # data = {
        #     'error_code': 0,
        #     'error_desc': '',
        #     'data': {
        #         'token': 'Q1uwyyokm5aKqkT63RujTbWiABiSTWdsfO3y+FZTQOvKujHSaTdHbKtQWZ9awv63E8QKLwOFZNhTOFzwB8ZqqEaL26yJ8IgKMV7/140asGAfDLq2/seJB+2/gXgZ4D5FmBrEUuE4LHjfX59uOP3++JyGLh6ldPyLtPzNRhRw5hmFHuQ3t7d+BlYTyI9IVRWcfnQaC41WLWibn+L9hqw0NcmCmutG7RjyE4nbv8umrXlkNx+uPCo4BfPIm9cVTy6QWqk3MFaX6mpGmFDW9dcz2jq5G78WftYiTxAl5819aGuUsnKRifIID5tu42Vw72/jursFS0hUFVA5EL+/s85By+BZlAxAfM4T6O37LKzChv5Xb9O+H53i5gwM1UkGvB6WCutXiyBrCRTQMjcYhw6+xgwpkG9U0dcC5Pad/bGZs2NrJFDDmHECOWG9aiEuCXu3y8FDjNioORwv7sYI0T4g4BEUXEfwEpjsKCj2AhrR5aUELNIGrNqC0QpfEr56JFTppAzBvkNTT4c5af4lQCEYpwXn6ErEVjj6xuAzJNsiRChm9Di91nAK27a+8mm7mjdLDpXEBn6TV5SMGt9JgRGAr4Wfcfj9QjgyFUxG0SOXmyJ+Hpq7QPWy5BKZp4oKswT5PtLRO+NiFmeuIn+qMUcZWCb043hInp778m0lOYMgshwmWFffzLJxGgELw4gh+sLTso/bnWCseCDsMszO4s5gYkPtgnkGQyEfydgsxWmYRtnART9htxLzgOQqzUI+FYmFkQ2LDW9+ppecJlrzJmjlTKuM5mC7VJeGscl/pyXhnwmlWmtHzgZzNds8fUsnfqlP9lpXRTUTRfdiGtthUm+i55F6w9IKmCxlPN3dvA10HrBuaJZxYzvJWzXmJIQe98l/CwTV4Bk1cEr8Lai5vM1FfFQC8bcfXEm0/ayENOXT49Ov1Y41HvFcva2fRYQVTe4R2cn7kvL0avihjAbkfraKnIEjh3miw1oK0DwhDEou5wcpvzcGN6tAgPGKrz15XJYgOx/bsaMD6opGwntBnqYOWIQ6I/zYCyKWbfACI65EhkS4i/4V6cMXdPAHMBPeLw0Q0VUYtcOOJ1MuruRfJOmlmWnoHXWWvyodPJm2Xx6UI3liOq4jOVbQhg87uAvQ9FWqWC/Vx0lsVbLHguH42vTWdL+dK1acXQfOB2QKZue2AVQlQCpcsen1NBZb7Tbhm4Zl81s5V2NzXYfIC/UqCWgYVVq2qN7wszaM72mdzPJSMWGFuAL9HDj4sEm1flRSSHNZRMtcLTgzdjBC+gc7xzrK9G7pRmcdINwouLa3Q1SegAF0kPj9xpZi3q9WSVBcX7W3rI1pJ3NwJuBOG6W9xzZHEUrkeFE1e0zn8yIh4Zh7Cyimw2THSjwli2kyWTmspzDnNrXU90F+NwURCiIyhVI/M6+jiiGCSazrTCDp8HUnuRkN039kF/PseqdLoAFJ9VLCHUCelpo+UnB1pzHO8Ni5K15UFSDU9GCBQSAwQ1Tyyxx4izbumqrmC2OjDfYZw0TaPzNQKpQ5THg4LFiJrc/Zx8B4e2tNYue97SZVKYdVUv4='
        #     }
        # }
        return Response(token_response)



# import os
# import django
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kampret.settings')
# django.setup()
# from tokenku.models import WsFeeder
#
# # Fetch all entries
# all_feeders = WsFeeder.objects.all()
# for feeder in all_feeders:
#     print(feeder.url, feeder.username, feeder.password)
