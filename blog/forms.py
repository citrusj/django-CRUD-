from django import forms

from .models import Post

class PostForm(forms.ModelForm):
    #file = forms.FileField(required = False)
    CHOICES = (('public','public'),('private','private'),)
    category = forms.ChoiceField(choices=CHOICES)
    
    class Meta:
        model = Post
        fields = ('title','text','filetwo','category')
        