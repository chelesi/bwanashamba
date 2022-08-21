from django import forms

class loginform(forms.form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)