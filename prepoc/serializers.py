from rest_framework import serializers
from .models import messages, messagesSummary, messagesList

class messagesListSerializer(serializers.ModelSerializer):
     class Meta:
          model = messagesList
          fields = ['messageId']

class messagesSerializer(serializers.ModelSerializer):
     class Meta:
          model = messages
          fields = ['messageId', 'message']

class messagesSummarySerializer(serializers.ModelSerializer):
     class Meta:
          model = messagesSummary
          fields = ['messageId','generationDate','endpoint','callMethods','messageSize','senderId','recipientId','callResponseTimeMs','callResponse']