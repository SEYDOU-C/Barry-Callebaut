from django import forms

class CallebautForms(forms.Form):
    username = forms.CharField( max_length= 50, required=True, label="Utilisteur")
    password = forms.CharField(max_length=10, required=True, label="Mot de passe")