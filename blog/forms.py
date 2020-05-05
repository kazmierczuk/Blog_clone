from django import forms
from blog.models import Post, Comment

class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('author', 'title', 'text')

        widgets = {
            'title':forms.TextInput(attrs={'class':'textinputclass'}),# my class
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})# postcontent is my custom class
        }


class CommmentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('author', 'text')

        # connecting forms to css styling
        widgets = {
            'author':forms.TextInput(attrs={'class':'textinputclass'}),# my class
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})# postcontent is my custom class
        }
