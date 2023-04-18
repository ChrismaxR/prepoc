from rest_framework import serializers
from .models import messages, messagesSummary, messagesList

class messagesListSerializer(serializers.ModelSerializer):
     class Meta:
          model = messagesList
          fields = ['id']

class messagesSerializer(serializers.ModelSerializer):
     class Meta:
          model = messages
          fields = ['id', 'message']

class messagesSummarySerializer(serializers.ModelSerializer):
     class Meta:
          model = messagesSummary
          fields = ['numberOfMessages','messageStatus','messagePriority']