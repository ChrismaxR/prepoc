from django.db import models

class persoonsLijst(models.Model):
    aNummer = models.CharField(max_length=100)
    bsn = models.CharField(max_length=100)
    naam = models.CharField(max_length=100)
    telefoon = models.CharField(max_length=100)
    geboorteDatum = models.CharField(max_length=100)
    geboortePlaats = models.CharField(max_length=100)
    geboorteLand = models.CharField(max_length=100)
    geslachtsaanduiding = models.CharField(max_length=100)
    nationaliteit1 = models.CharField(max_length=100)
    nationaliteit2 = models.CharField(max_length=100)
    huidigePostcode = models.CharField(max_length=100)
    huidigeHuisnummer = models.CharField(max_length=100)
    huidigeWoonplaats = models.CharField(max_length=100)
    huidigeAdresGeldig = models.CharField(max_length=100)
    vorigePostcode = models.CharField(max_length=100)
    vorigeHuisnummer = models.CharField(max_length=100)
    vorigeWoonplaats = models.CharField(max_length=100)
    vorigeAdresGeldig = models.CharField(max_length=100)
    volgnummer = models.CharField(max_length=100)

    def __str__(self):
        return self.naam + " - " + self.volgnummer

class messages(models.Model):
    messageId = models.CharField(max_length=50)
    recipientId = models.CharField(max_length=50)
    message = models.JSONField()

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
