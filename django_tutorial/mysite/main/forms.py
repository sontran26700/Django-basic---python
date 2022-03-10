from django import forms

class CreateNewList(forms.Form):
	name = forms.CharField(label="Name")
	check = forms.BooleanField(required=False)

