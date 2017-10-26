from rest_framework import serializers
from .models import BusinessProfile

class BusinessProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = BusinessProfile
        fields = ('companyType', 'registeredName', 'companyName',
                  'dateFiled', 'address', 'city', 'state', 'zipCode')