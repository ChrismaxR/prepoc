from django.contrib import admin
from .models import messagesList, messages, messagesSummary

admin.site.register(messagesList)
admin.site.register(messages)
admin.site.register(messagesSummary)