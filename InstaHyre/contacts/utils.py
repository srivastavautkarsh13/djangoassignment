# Django imports.
from django.db.models import Q 

# App imports.
from users.models import User
from contacts.models import Contacts
from contacts.serializers import (
	UserContactSerializer,
	ContactsSerializer
)


def search_contacts_for_name(searched_name):
	
    user_qs = User.objects.filter(
        Q(name__startswith = searched_name)|
        Q(name__icontains = searched_name)
    ).distinct()
    contact_qs = Contacts.objects.filter(
        Q(name__startswith = searched_name)|
        Q(name__icontains = searched_name)
    ).distinct()
    users_serializer = UserContactSerializer(user_qs,many=True)
    contacts_serializer = ContactsSerializer(contact_qs, many=True)
    final_data=dict(
    	registered_users = users_serializer.data,
        personal_contacts = contacts_serializer.data
    )
    return final_data


def search_contacts_for_number(searched_number):
    user_qs = User.objects.filter(phone_number=searched_number)
    if user_qs.exists():
        person = user_qs.first()
        user_serializer = UserContactSerializer(person)
        return user_serializer.data 
    else:
        contacts_qs = Contacts.objects.filter(
        					phone_number=searched_number
        				)
        if contacts_qs.exists():
            serializer = ContactsSerializer(contacts_qs, many=True)
            final_data= dict(
				message="An unregistered contact number",
                data=serializer.data
            )
            return final_data
        return dict()