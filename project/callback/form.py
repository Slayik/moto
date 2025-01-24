# callback/forms.py
from django import forms

class CallbackForm(forms.Form):
    name = forms.CharField(label="Ваше имя", max_length=100)
    phone_number = forms.CharField(label="Ваш номер телефона", max_length=20)
    email = forms.EmailField(label="Ваш email")  # поле для email
    message = forms.CharField(label="Сообщение", widget=forms.Textarea, required=False)
