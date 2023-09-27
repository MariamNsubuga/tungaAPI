from django.shortcuts import render

from rest_framework.decorators import api_view

from rest_framework.response import Response

from django.http import HttpRequest,JsonResponse

from .serializers import *

from .models import *
# Create your views here.

@api_view(['GET','POST'])# allows django rest framework to map request and respone 

def hello_world(request):
    if request.method == "POST":
        return Response(request.data)
        # return Response({"message":request.data})
        # return Response({request.data})
    return Response({"message": "Hello,world"},status=200)
    # return Response( "Hello,world",status=200)
'''
def hello_world(request):
    if request.method == "POST":
        return Response(request.data)
        # return Response({"message":request.data})
        # return Response({request.data})
    return Response({"message": "Hello,world"},status=200)
    # return Response( "Hello,world",status=200)
    '''
@api_view(['GET','POST'])
def post_list(request):
    posts= Post.objects.all()
    serilazed_post = PostSerializer(posts, many=True).data
    return Response(serilazed_post)