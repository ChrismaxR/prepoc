from django.db import models

class messages(models.Model):
    messageId = models.CharField(max_length=50, blank=True, null=True)
    recipientId = models.CharField(max_length=50, blank=True, null=True)
    message = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.messageId

class messagesSummary(models.Model):
    messageId = models.CharField(max_length=100)
    generationDate = models.CharField(max_length=100)
    endpoint = models.CharField(max_length=100)
    callMethods = models.CharField(max_length=100)
    messageSize = models.CharField(max_length=100)
    senderId = models.CharField(max_length=100)
    recipientId = models.CharField(max_length=100)
    callResponseTimeMs = models.CharField(max_length=100)
    callResponse = models.CharField(max_length=100)

    def __str__(self):
        return self.messageId

class messagesList(models.Model):
    messageId = models.CharField(max_length=50)

    def __str__(self):
        return self.messageId
