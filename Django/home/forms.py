from django.forms import ModelForm
from .models import Product
from django import forms

from django.contrib.auth.forms import AuthenticationForm

class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))



class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = [
            'lesson_name',
            'lesson_number',
            'videoId',
            'description',
            'telegram',
            'youtube',
            # 'category_name',
            'subcategory_name',
            ]
        widgets = {
            'lesson_name': forms.TextInput(attrs={'class': 'form-control w-100', "id":"floatingInput"}),
            'lesson_number': forms.NumberInput(attrs={'class': 'form-control w-100',}),
            'description': forms.Textarea(attrs={'class': 'form-control w-100', "id":"exampleFormControlTextarea1" , "rows":"3"}),
            'videoId': forms.TextInput(attrs={'class': 'form-control w-100' }),
            'telegram': forms.TextInput(attrs={'class': 'form-control w-100'}),
            'youtube': forms.TextInput(attrs={'class': 'form-control w-100'}),
            # 'category_name': forms.TextInput(attrs={'class': 'form-control w-100'}),
            'subcategory_name': forms.TextInput(attrs={'class': 'form-control w-100'}),

        }
        def clean_videoId(self):
            videoId = self.cleaned_data.get('videoId')
        # Add custom validation logic if needed
            return videoId
        

class SimpleProductForm(ModelForm):

    class Meta:
        model = Product
        fields = [
            'lesson_name',
            'lesson_number',
            'videoId',
            'description',
            'telegram',
            'youtube',
            # 'category_name',
            # 'subcategory_name',
            ]
        widgets = {
            'lesson_name': forms.TextInput(attrs={'class': 'form-control w-100', "id":"floatingInput"}),
            'lesson_number': forms.NumberInput(attrs={'class': 'form-control w-100',}),
            'description': forms.Textarea(attrs={'class': 'form-control w-100', "id":"exampleFormControlTextarea1" , "rows":"3"}),
            'videoId': forms.TextInput(attrs={'class': 'form-control w-100' }),
            'telegram': forms.TextInput(attrs={'class': 'form-control w-100'}),
            'youtube': forms.TextInput(attrs={'class': 'form-control w-100'}),
            # 'category_name': forms.TextInput(attrs={'class': 'form-control w-100'}),
            # 'subcategory_name': forms.TextInput(attrs={'class': 'form-control w-100'}),
        }
        def clean_videoId(self):
            videoId = self.cleaned_data.get('videoId')
        # Add custom validation logic if needed
            return videoId
