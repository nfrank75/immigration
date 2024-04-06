from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Nom', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    phone = forms.CharField(label='Phone', max_length=100)
    pays = forms.CharField(label='Pays', max_length=100)
    message = forms.CharField(label='Message', widget=forms.Textarea)
    pays = forms.CharField(label='Subjet')