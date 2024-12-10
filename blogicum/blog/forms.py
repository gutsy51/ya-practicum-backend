from django import forms
from django.contrib.auth import get_user_model

from blog.models import Post


User = get_user_model()


class PostForm(forms.ModelForm):
    """New post form."""
    class Meta:
        model = Post
        exclude = ('author', 'created_at',)
        widgets = {
            'pub_date': forms.DateTimeInput(format='%Y-%m-%dT%H:%M',
                                            attrs={'type': 'datetime-local'})
        }


class ProfileEditForm(forms.ModelForm):
    """Update user data form."""
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')