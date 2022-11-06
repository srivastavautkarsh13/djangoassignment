# Django imports.
from django.urls import path

from contacts.views import (
	SetSpamContactView, 
	ContactSearchView,
	UserDetailProfileView, 
)


urlpatterns = [
    path('spam/', SetSpamContactView.as_view(), name='set-spam'),
    path('search/', ContactSearchView.as_view(), name='contact-search'),
    path('detail/<int:user_id>/', UserDetailProfileView.as_view(), name='detailed-view')

]