from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.core.mail import send_mail

from contact_form.models import Contact

# Функция отправки сообщения
def email(subject, content):
    send_mail(subject, content, 'auto-message@neptun55.ru', ['vet.omsk@mail.ru'])

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"

    def create(self, validated_data):
        contact = Contact(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone=validated_data['phone'],
            locality=validated_data['locality'],
            message=validated_data['message']
        )
        # contact.set_password(validated_data['password'])

        if contact.last_name == '':
            print('Фамилия пуста, отправляем письмо')
            print(contact.first_name)
            print(contact.email)
            subject = f'Сообщение с сайта от {contact.first_name}, Телефон: {contact.phone} Почта отправителя: {contact.email}'
            email(subject, contact.message + 'Телефон: ' + contact.phone)
        else:
            print('Фамилия введена, не отправляем письмо')


        contact.save()
        return contact

    # def mail_if_valid(self, validated_data):
    #     # Формируем сообщение для отправки
    #     contact = Contact(
    #         email=validated_data['email'],
    #         first_name=validated_data['first_name'],
    #         last_name=validated_data['last_name'],
    #         phone=validated_data['phone'],
    #         locality=validated_data['locality'],
    #         message=validated_data['message']
    #     )
    #     if contact.last_name == '':
    #         print('Фамилия пуста, отправляем письмо')
    #         subject = f'Сообщение с сайта от {contact.first_name}, Телефон: {contact.phone} Почта отправителя: {contact.email}'
    #         email(subject, contact.message + 'Телефон: ' + contact.phone)
    #         return super().form_valid(form)
    #     else:
    #         print('Фамилия введена, не отправляем письмо')
