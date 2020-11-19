from django import forms

from nomenclature.models import Service, Profile, UploadFiles


class UploadFilesForm(forms.ModelForm):
    class Meta:
        model = UploadFiles
        fields = ('file', )


class ServiceEditForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

    services = forms.ModelMultipleChoiceField(queryset=Service.objects.all())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
