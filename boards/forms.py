from django import forms
from .models import Topic, Post, Board, GalleryImages
from django.core.files import File
from PIL import Image
from accounts.models import User, Photo



class GalleryImagesForm(forms.ModelForm):
    image = forms.FileField(widget=forms.FileInput)
    class Meta:
        model = GalleryImages
        fields = ('image',)
class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User    
        fields = ("first_name", 'last_name', 'email')


class NewTopicForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'placeholder': 'What is on your mind?'}),
                              max_length=4000,
                              help_text='The max length of the text is 4000')

    class Meta:
        model = Topic
        fields = ('subject', 'message')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('message', )


class BoardCreateForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ('name', 'description')
