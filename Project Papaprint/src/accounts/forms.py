from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)
User = get_user_model()
class UserLoginForm(forms.Form):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'required': 'required', 'placeholder': 'Username', 'autocomplete': 'off','pattern':'[A-Za-z]([A-Za-z]{4}|[A-Za-z][0-9]|[0-9]{4})[0-9]{0,6}$', 'title':'Username must be Up to 5 to 9 digits to be allowed.'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError("Incorrect username or password")
        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserSignupForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, label='First name', widget=forms.TextInput(attrs={'class': 'form-control', 'required': 'required', 'placeholder': 'Enter firstname'}))
    last_name = forms.CharField(max_length=150, label='Last name', widget=forms.TextInput(attrs={'class': 'form-control', 'required': 'required', 'placeholder': 'Enter lastname'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'required': 'required', 'placeholder': 'Enter Username', 'autocomplete': 'off','pattern':'[a-zA-Z0-9]{5,9}$', 'title':'Username must be Up to 5 to 9 digits to be allowed.'}))
    email2 = forms.EmailField(label='Confirm Email Address', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password', 'pattern': '(?=^.{8,}$)((?=.*\d)|(?=.*\W+))(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$', 'title':'Required. Must contain at least 1 uppercase character, must contain at least 1 number. Up to to 8 digits to be allowed.'}))
    email = forms.EmailField(label='Email Address', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}))
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'email2',
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


