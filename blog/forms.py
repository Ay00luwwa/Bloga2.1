from django import forms
from .models import Post, Category, BlogImage

class SearchForm(forms.Form):
    query = forms.CharField()

class PostForm(forms.ModelForm):
    new_category = forms.CharField(
        required=False, 
        widget=forms.TextInput(attrs={'placeholder': 'Add new category'})
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'image', 'category', 'new_category']

    def clean(self):
        cleaned_data = super().clean()
        category = cleaned_data.get('category')
        new_category = cleaned_data.get('new_category')

        if not category and not new_category:
            raise forms.ValidationError('Either select a category or add a new one.')

        return cleaned_data

