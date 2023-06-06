from django import forms
from django.contrib.auth.models import User

from cars.models import Event, Car


class CarEventForm(forms.ModelForm):
    km_of_car = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control input-custom', 'placeholder': 'КМ на автомобила'}))
    event_text = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control input-custom', 'placeholder': 'Причина за посещението'}))
    next_date = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control input-custom', 'placeholder': 'Следваща дата на посещение'}), required=False)
    periodic_event = forms.BooleanField(
        widget=forms.CheckboxInput(), required=False)

    class Meta:
        model = Event
        fields = ['km_of_car', 'event_text', 'periodic_event', 'next_date']

    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data['next_date'] == '':
            cleaned_data['next_date'] = None

        return cleaned_data


class CarForm(forms.ModelForm):
    model = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control input-custom'}))
    maker = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control input-custom'}))
    year_of_make = forms.DateField(
        widget=forms.DateInput(
            {'class': 'form-control input-custom', 'type': 'date'}
        )
    )
    registration_number = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control input-custom'}))
    user = forms.ModelChoiceField(queryset=User.objects.filter(is_staff=False, is_superuser=False),
                                  widget=forms.Select(attrs={'class': 'input-custom'}),
                                  required=False)
    in_service = forms.BooleanField(
        widget=forms.CheckboxInput(), required=False
    )

    class Meta:
        model = Car
        fields = [
            'model',
            'maker',
            'year_of_make',
            'registration_number',
            'user',
            'in_service'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].queryset = User.objects.filter(is_staff=False, is_superuser=False)

    def save(self, commit=True):
        car_instance = super().save(commit=False)
        car_instance.user = self.cleaned_data['user']
        if commit:
            car_instance.save()
        return car_instance
