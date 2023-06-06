from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import TextInput, PasswordInput

from cars.models import ServiceRequest, InvitedUserCarRequest, ContactFormModel


class UserRegistrateForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Име'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Фамилия'}))
    phone = forms.CharField(min_length=10, max_length=10,
                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Телефон'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Парола'}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Парола потвърди'}))

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'phone',
            'password1',
            'password2',
        ]

    def save(self, commit=True):
        user = super(UserRegistrateForm, self).save(commit=False)
        user.username = user.email

        if commit:
            user.save()
        return user


class ServiceRequestForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control input-custom', 'placeholder': 'Име'}))
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control input-custom', 'placeholder': 'Фамилия'}))
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'class': 'form-control input-custom', 'placeholder': 'Email'}))
    phone = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control input-custom', 'placeholder': 'Телефон'}), max_length=10)
    request_text = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control textarea-custom', 'placeholder': 'Необходимо обслужване или ремонт...'}))

    class Meta:
        model = ServiceRequest
        fields = [
            'first_name',
            'last_name',
            'email',
            'phone',
            'request_text',
        ]


class InvitedUserCarRequestForm(forms.ModelForm):
    class Meta:
        model = InvitedUserCarRequest
        fields = [
            'car_registration_number',
            'other_info'
        ]


class CustomLoginAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget = TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
        self.fields['password'].widget = PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Парола'})


class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input-custom input-full', 'placeholder': 'Име'}))
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input-custom input-full', 'placeholder': 'Фамилия'}))
    phone = forms.CharField(max_length=10,
                            widget=forms.TextInput(
                                attrs={'class': 'input-custom input-full', 'placeholder': 'Вашия телефон'}))
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'class': 'input-custom input-full', 'placeholder': 'E-mail'}))
    text = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'input-custom input-full', 'placeholder': 'Вашето съобщение'}))

    class Meta:
        model = ContactFormModel
        fields = ['first_name', 'last_name', 'phone', 'email', 'text']
