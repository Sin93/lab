from django import forms
from django.contrib.auth.forms import AuthenticationForm, ValidationError, UserCreationForm, UserChangeForm
from authapp.models import LabUser


class LabUserLoginForm(AuthenticationForm):
    class Meta():
        model = LabUser
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(LabUserLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class LabUserRegisterForm(UserCreationForm):
    class Meta():
        model = LabUser
        fields = (
            'username',
            'first_name',
            'password1',
            'password2',
            'email',
            'position'
        )

    def __init__(self, *args, **kwargs):
        super(LabUserRegisterForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError('Вы слишком молоды!')
        return data


class LabUserEditForm(UserChangeForm):
    class Meta(object):
        model = LabUser
        fields = ('username', 'first_name', 'email', 'position')

    def __init__(self, *args, **kwargs):
        super(LabUserEditForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
            if field_name == 'password':
                field.widget = forms.HiddenInput()
