from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import info
from .models import Characters


class CharacterView(APIView):
    def get(self,request):
        if 'character' in request.GET:
            q=request.GET['character'].upper()
            print(q)
            data=info.getCharacters(q)


        else:
            data={"Error":"Unable to fetch data, try again"}
        return Response(data,status=200)
    def post(self,request):
        details=request.data
        Characters.objects.create(name=details['name'],starting_alhphabet=details['starting_alhphabet'])
        data={"Message":"created"}
        return Response(data,status=202)
    def obtain(self,request):
        if 'character' in request.GET:
            qq=request.GET['character'].upper()
            data=info.getCharacters(qq)
            return data
        else:
            data={"Error":"Unable to fetch data, try again"}
            return data





class CharacterImageView(APIView):
    def get(self,request):
        if 'character_image' in request.GET:
            data=info.getCharacterImage(request.GET['character_image'])

        else:
            data={"Error":"Unable to fetch data, try again"}
        return Response(data,status=200)
