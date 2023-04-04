from rest_framework import serializers
from .models import persoonsLijst

class persoonsLijstSerializer(serializers.ModelSerializer):
     class Meta:
          model = persoonsLijst
          fields = ['aNummer','bsn','naam','telefoon','geboorteDatum','geboortePlaats','geboorteLand','geslachtsaanduiding','nationaliteit1','nationaliteit2','huidigePostcode','huidigeHuisnummer','huidigeWoonplaats','huidigeAdresGeldig','vorigePostcode','vorigeHuisnummer','vorigeWoonplaats','vorigeAdresGeldig','volgnummer']