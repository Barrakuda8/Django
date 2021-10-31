from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms
from authapp.models import Player


class PlayerLoginForm(AuthenticationForm):

    class Meta:
        model = Player
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''


class PlayerRegisterForm(UserCreationForm):

    class Meta:
        model = Player
        fields = ('username', 'nickname', 'age', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

    def clean_nickname(self):
        data = self.cleaned_data['nickname']
        if 'fuck' in data:
            raise forms.ValidationError('Restricted words in your nickname')
        return data


class PlayerEditForm(UserChangeForm):

    class Meta:
        model = Player
        fields = ('username', 'nickname', 'age', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
            if field_name == 'password':
                field.widget = forms.HiddenInput()

    def clean_nickname(self):
        data = self.cleaned_data['nickname']
        if 'fuck' in data:
            raise forms.ValidationError('Restricted words in your nickname')
        return data
