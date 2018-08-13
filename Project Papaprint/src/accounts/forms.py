from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)
User = get_user_model()
class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError("Incorrect username or password")
        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserSignupForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}))
    email2 = forms.EmailField(label='Email Address', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Confirm Email Address', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = [
            'username',
            'email2',
            'email',
            'password'
        ]
    def clean(self, *args, **kwargs):
        print(self.cleaned_data)
        email = self.cleaned_data.get('email'),
        email2 = self.cleaned_data.get('email2'),
        print(email, email2)
        if User.objects.filter(username=self.cleaned_data['username']).exists():
            raise forms.ValidationError('username already exist')
        if not email == email2:
            raise forms.ValidationError ('Email must match')
        email_qs = User.objects.filter (email='email')
        if email_qs.exists():
            raise forms.ValidationError ('This email is already been registered')
        return super(UserSignupForm, self).clean(*args, **kwargs)
