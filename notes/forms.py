from django import forms
from.models import myBlogs, myComments

class BlogForm(forms.ModelForm):
    class Meta:
        model= myBlogs
        fields = ['title','content', 'image']

class CommentForm(forms.ModelForm):
    class Meta:
        model = myComments
        fields = ['content']

