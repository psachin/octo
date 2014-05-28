from django import forms
from models import Blog

# begin forms
class PostForm(forms.ModelForm):
    title = forms.CharField()
    body = forms.TextInput()

    class Meta:
        model = Blog
        fields = ['title', 'body']

        


