from django.forms import ModelForm
from django.forms import Textarea, TextInput
from .models import Contact
from django import forms

# from snowpenguin.django.recaptcha3.fields import ReCaptchaField



class ContactForm(forms.ModelForm):
    # captcha = ReCaptchaField
    class Meta:
        # Определяем модель, на основе которой создаем форму
        model = Contact
        # Поля, которые будем использовать для заполнения
        fields = ['first_name', 'last_name', 'email', 'phone', 'locality', 'message']
        widgets = {
            'message': Textarea(
                attrs={
                    'placeholder': 'Напишите тут ваше сообщение'
                }
            ),
            'first_name': TextInput(
                attrs={
                    'placeholder': 'Ваше имя: '
                }
            ),
            'last_name': TextInput(
                attrs={
                    'placeholder': 'Ваша фамилия: '
                }
            ),
            'email': TextInput(
                attrs={
                    'placeholder': 'Ваш е-мейл: '
                }
            ),
            'locality': TextInput(
                attrs={
                    'placeholder': 'Населенный пункт: '
                }
            ),
            'phone': TextInput(
                attrs={
                    'placeholder': 'Ваш телефон: '
                }
            ),
        }