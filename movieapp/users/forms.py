from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
import random

from .models import Profile


class ChangePasswordForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["old_password"].widget = forms.widgets.PasswordInput(attrs={"class":"form-control"})
        self.fields["new_password1"].widget = forms.widgets.PasswordInput(attrs={"class":"form-control"})
        self.fields["new_password2"].widget = forms.widgets.PasswordInput(attrs={"class":"form-control"})            


class UserForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={"class":"form-control form-control-user","placeholder":"Enter Email adress"}),)
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control form-control-user","placeholder":"Enter the Password"}))
    remember_me = forms.BooleanField(required=False,initial=False, widget=forms.CheckboxInput(attrs={"class":"custom-control-input"}))
    
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not User.objects.filter(email__iexact = email).exists():
            self.add_error("email","Bele bir email movcud deildir.")
        
        return email



class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email","first_name","last_name")
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields["first_name"].widget = forms.TextInput(attrs={"class":"form-control form-control-user","placeholder":"Firtsname"})
        self.fields["last_name"].widget = forms.TextInput(attrs={"class":"form-control form-control-user","placeholder":"Lastname"})
        self.fields["email"].widget = forms.EmailInput(attrs={"class":"form-control form-control-user","placeholder":"Email"})
        self.fields["password1"].widget = forms.PasswordInput(attrs={"class":"form-control form-control-user","placeholder":"Password1"})
        self.fields["password2"].widget = forms.PasswordInput(attrs={"class":"form-control form-control-user","placeholder":"Password2"})
        self.fields["email"].required = True
        self.fields["first_name"].required = True
        self.fields["last_name"].required = True
        
        
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email = email).exists():
            self.add_error("email", "Bele bir email movcuddur.")
        return email
    
    
    def save(self, commit=True):
        user = super(UserCreationForm,self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.username = "{}_{}_{}".format(
            self.cleaned_data.get("first_name").lower(),
            self.cleaned_data.get("last_name").lower(),
            random.randint(11111,99999)
        )
        
        if commit:
            user.save()
            
        return user
    
    
    
class UserModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name","last_name","email")
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields["first_name"].widget = forms.TextInput(attrs={"class":"form-control form-control-user","placeholder":"Firtsname"})
        self.fields["last_name"].widget = forms.TextInput(attrs={"class":"form-control form-control-user","placeholder":"Lastname"})
        self.fields["email"].widget = forms.EmailInput(attrs={"class":"form-control form-control-user","placeholder":"Email"})
        
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("location","avatar",)
        
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        
        self.fields["location"].widget = forms.TextInput(attrs={"class":"form-control","placeholder":"Location"})