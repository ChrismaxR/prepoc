from django.db import models

class messages(models.Model):
    messageId = models.CharField(max_length=50, blank=True, null=True)
    recipientId = models.CharField(max_length=50, blank=True, null=True)
    message = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.messageId

class messagesSummary(models.Model):
    numberOfMessages = models.IntegerField(blank=True, null=True)
    messageStatus = models.CharField(max_length=50, blank=True, null=True)
    messagePriority = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.messageId

class messagesList(models.Model):
    messageId = models.CharField(max_length=50)

    def __str__(self):
        return self.messageId
