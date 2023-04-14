from rest_framework import serializers
from .models import persoonsLijst
from .models import messages

class persoonsLijstSerializer(serializers.ModelSerializer):
     class Meta:
          model = persoonsLijst
          fields = ['aNummer','bsn','naam','telefoon','geboorteDatum','geboortePlaats','geboorteLand','geslachtsaanduiding','nationaliteit1','nationaliteit2','huidigePostcode','huidigeHuisnummer','huidigeWoonplaats','huidigeAdresGeldig','vorigePostcode','vorigeHuisnummer','vorigeWoonplaats','vorigeAdresGeldig','volgnummer']

class messagesSerializer(serializers.ModelSerializer):
     class Meta:
          model = messages
          fields = ['messageId','message']