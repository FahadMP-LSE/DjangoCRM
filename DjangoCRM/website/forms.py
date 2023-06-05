from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User# User is user model - to get user details built-in.
from django import forms


class SignUpForm(UserCreationForm):# the class is importing the UserCreationForm but want to also modify a bit
    email= forms.EmailField(label="",widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Email Address"})) # getting user email address - can get @ symbol
    #label="" is because we will ahve our own placeholder text and don't want anything showing here by default
    #widget=forms.TextInput() means that the form field appears on screen..that is a text input field. - a text box
    #attrs=attribute...using bootstrap to style our forms
    first_name=forms.CharField(label="",max_length=100,widget=forms.TextInput(attrs={"class":"form-control","placeholder":"First Name"}))# just getting names - no @ needed here
    last_name=forms.CharField(label="",max_length=100,widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Last Name"}))
    #max length is for max characters e.g. name cannot be more than 100 characters long

    class Meta:
        model=User
        fields=("username","first_name","last_name","email","password1","password2")


    def __init__(self, *args, **kwargs):#doing same thing as above but for all username, password1, password 2
        super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'User Name'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'
#help text is to help incase someone inputs wrong information.
		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'
#help text is to help incase someone inputs wrong information.
		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	


