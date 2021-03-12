from django.urls import path

from . import views
import contacts

urlpatterns = [
    path('contact',views.contact,name='contact')
]