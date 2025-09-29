from django import forms
from.models import myBlogs, myComments
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150,label="Username")
    password = forms.CharField(widget=forms.PasswordInput,label="Password")


class SignupForm(UserCreationForm):


    class Meta:
        model = User
        fields = ['username', 'email','password1','password2']

        # def clean(self):
        #     cleaned_data = super().clean()
        #     password = cleaned_data.get("password")
        #     confirm_password = cleaned_data.get("confirm_password")
        #     if password != confirm_password:
        #         self.add_error('confirm_password', "Passwords don't match")





class BlogForm(forms.ModelForm):
    class Meta:
        model= myBlogs
        fields = ['title','content', 'image']

class CommentForm(forms.ModelForm):
    class Meta:
        model = myComments
        fields = ['content']

