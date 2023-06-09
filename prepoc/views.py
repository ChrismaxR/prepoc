from django.http import JsonResponse
from .models import messages, messagesSummary
from .serializers import messagesSerializer, messagesSummarySerializer, messagesListSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# messages calls
## List messages
@api_view(['GET'])
def listMessages(request):

    if request.method == 'GET':
        lms = messages.objects.all()
        serializer = messagesListSerializer(lms, many=True)
        return Response(serializer.data)

## Bulk messages
@api_view(['GET', 'POST'])
def bulkMessages(request):
    
    if request.method == 'GET':
        ms = messages.objects.all()
        serializer = messagesSerializer(ms, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = messagesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


## Get messages calls    
@api_view(['GET'])
def getMessages(request, id):

    try:
        ms = messages.objects.get(pk=id)
    except messages.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = messagesSerializer(ms)
        return Response(serializer.data)
    
    # commented out, denk niet dat ik deze call nodig heb in de prototype
    #elif request.method == 'PUT':
    #    serializer = messagesSerializer(ms, data=request.data)
    #    if serializer.is_valid():
    #        serializer.save()
    #        return Response(serializer.data)
    #    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# messagesSummary call

@api_view(['GET'])
def summarizeMessages(request):

    if request.method == 'GET':
        mss = messagesSummary.objects.all()
        serializer = messagesSummarySerializer(mss, many=True)
        return Response(serializer.data)

