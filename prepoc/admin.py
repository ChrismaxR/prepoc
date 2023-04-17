from django.contrib import admin
from .models import persoonsLijst, messages, messagesSummary

admin.site.register(persoonsLijst)
admin.site.register(messages)
admin.site.register(messagesSummary)