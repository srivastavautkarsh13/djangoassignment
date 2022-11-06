# DRF imports.
from rest_framework import serializers

# App imports.
from users.models import User
from contacts.models import Contacts


class UserContactSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('id', 'name', 'phone_number', 'spam_flag')


class ContactsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Contacts
        fields = ('id', 'name', 'phone_number', 'spam_flag')
