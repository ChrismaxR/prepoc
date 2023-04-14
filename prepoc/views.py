from django.http import JsonResponse
from .models import persoonsLijst
from .models import messages
from .serializers import persoonsLijstSerializer
from .serializers import messagesSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def persoonsLijst_list(request):

    if request.method == 'GET':
        pl = persoonsLijst.objects.all()
        serializer = persoonsLijstSerializer(pl, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = persoonsLijstSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def persoonsLijst_details(request, id):

    try:
        pl = persoonsLijst.objects.get(pk=id)
    except persoonsLijst.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = persoonsLijstSerializer(pl)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = persoonsLijstSerializer(pl, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        pl.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#messages calls
@api_view(['GET', 'POST'])
def listMessages(request):

    if request.method == 'GET':
        ms = messages.objects.all()
        serializer = messagesSerializer(ms, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = messagesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        
@api_view(['GET', 'PUT', 'DELETE'])
def getMessages(request, id):

    try:
        ms = messages.objects.get(pk=id)
    except messages.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = messagesSerializer(ms)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = messagesSerializer(ms, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        ms.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)