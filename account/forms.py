from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User



# Create your models here.




class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = [ 'username', 'email', 'password1', 'password2']

    def clean_password2(self):
        pswrd1 = self.cleaned_data['password1']
        pswrd2 = self.cleaned_data['password2']
        if pswrd1 == pswrd2:
            if len(pswrd2) < 8 :
                raise forms.ValidationError('Password must be at least eigth character.')
            return pswrd2
        raise forms.ValidationError("Passwords didn't match")