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

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class TokenView(APIView):

    def get(self, request):
        from tokenku.models import WsFeeder
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
