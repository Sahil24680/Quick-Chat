from django import forms

class ProfilePictureForm(forms.Form):
    profile_img = forms.ImageField()
