from django.shortcuts import render
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def list(request):
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def detail(request, pk):
    events = Event.objects.all()
    serializer = EventSerializer(events, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def create(request):
    serializer = EventSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def update(request,pk):
    event = Event.objects.get(id=pk)
    serializer = EventSerializer(instance=event, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def Deletes(request,pk):
    event = Event.objects.get(id=pk)
    event.delete()
    return Response('Deleted')