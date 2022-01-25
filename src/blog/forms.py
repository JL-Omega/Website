from .models import BlogPost
from django import forms


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'created_on', 'author', 'content']

        labels = {
            'title': 'Titre',
            'created_on': 'Date de création',
            'content': 'Contenu',
            'author': 'Auteur'
        }

        widgets = {'created_on': forms.SelectDateWidget(years=range(2000, 20100))}

