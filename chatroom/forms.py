from django import forms
from chatroom import models as chatroom_model

class CreateroomForm(forms.ModelForm):

    class Meta:
        model = chatroom_model.Room
        fields = ['rname','rimage','rdescription','rcourse', 'rcollege']
        widgets = {
            'rcourse':forms.CheckboxSelectMultiple,
            'rcollege':forms.CheckboxSelectMultiple
        }
        labels = {
            'rname':'Name',
            'rimage':'Image',
            'rdescription': 'Description',
            'rcourse':'Course',
            'rcollege':'College'

        }
