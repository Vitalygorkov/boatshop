from django.forms import ModelForm
from django.forms import Textarea, TextInput
from .models import Contact
from django import forms
# from captcha.fields import CaptchaField

# from snowpenguin.django.recaptcha3.fields import ReCaptchaField



class ContactForm(forms.ModelForm):
    # captcha = CaptchaField()
    class Meta:
        # Определяем модель, на основе которой создаем форму
        model = Contact
        # Поля, которые будем использовать для заполнения
        fields = ['first_name', 'last_name', 'email', 'phone', 'locality', 'message']
        widgets = {
            'message': forms.Textarea(
                attrs={
                    'placeholder': 'Напишите тут ваше сообщение'
                }
            ),
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Ваше имя: '
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Ваша фамилия: '
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Ваш е-мейл: '
                }
            ),
            'locality': forms.TextInput(
                attrs={
                    'placeholder': 'Населенный пункт: '
                }
            ),
            'phone': forms.NumberInput(
                attrs={
                    'placeholder': 'Ваш телефон: '
                }
            ),
        }