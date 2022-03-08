from django.urls import path
from .views import ContactFormView, success


urlpatterns = [
    path('contact_form/', ContactFormView.as_view(), name='contact_view'),
    # path('success/', success, name='success_page'),

]