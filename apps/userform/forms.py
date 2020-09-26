from django import forms
from .models import Kariyer

class cvForm(forms.ModelForm):
    class Meta:
        model = Kariyer
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(cvForm, self).__init__(*args, **kwargs)
        for arr in self.fields:
            self.fields[arr].widget.attrs.update({'class': 'form__field' }, )