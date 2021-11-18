from authapp.forms import PlayerEditForm
from authapp.models import Player
from django import forms

from mainapp.models import CollectionCategory


class PlayerEditAdminForm(PlayerEditForm):

    class Meta:
        model = Player
        fields = '__all__'


class CategoryEditForm(forms.ModelForm):

    class Meta:
        model = CollectionCategory
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
