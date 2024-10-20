from django import forms

from blog.models import Post


class UserForm(forms.Form):
    name = forms.CharField(label='Введите имя')


class AddPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['text', 'author']

        widgets = {
            'text': forms.Textarea(attrs={'cols': 50, 'rows': 3})}
