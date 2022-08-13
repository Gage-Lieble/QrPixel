from rest_framework import serializers
from qruser_app.models import *

class QrSaverSerializer(serializers.ModelSerializer):
    class Meta:
        model = QrSaver
        fields = '__all__'