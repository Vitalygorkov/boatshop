from django.shortcuts import render, redirect
from .forms import ContactForm
from django.views.generic import CreateView, View
from .models import Contact
from .forms import ContactForm
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.http import HttpResponse
# Функция отправки сообщения
def email(subject, content):
    send_mail(subject, content, 'auto-message@neptun55.ru', ['vet55omsk@gmail.com'])

class ContactFormView(CreateView):
    model = Contact
    form_class = ContactForm
    success_url = "/success/"
    # success_url = reverse_lazy('success_page')
    def form_valid(self, form):
        # Формируем сообщение для отправки
        data = form.data
        if data["last_name"] == '':
            subject = f'Сообщение с сайта от {data["first_name"]} {data["last_name"]}, Телефон: {data["phone"]} Почта отправителя: {data["email"]}'
            email(subject, data['message'] + 'Телефон: ' + data['phone'])
            return super().form_valid(form)
        else:
            print('last name input')
            print(str(data["last_name"]))
            return super().form_valid(form)
        # data = form.data
        # subject = f'Сообщение с сайта от {data["first_name"]} {data["last_name"]}, Телефон: {data["phone"]} Почта отправителя: {data["email"]}'
        # email(subject, data['message'] + 'Телефон: ' + data['phone'])
        # return super().form_valid(form)

# Функция, которая вернет сообщение в случае успешного заполнения формы
def success(request):
   return HttpResponse('Письмо отправлено!')

