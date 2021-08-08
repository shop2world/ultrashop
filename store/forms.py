from django import forms
from django.forms import fields
from .models import Product,Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        labels = {
            'name': '성함',
            'description': '제품설명',
            'price': '가격',
            'digital': '디지탈제품',
            'image': '상품이미지',
        }


class CreateUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username","email","password1","password2")

    def save(self, commit=True):
        user = super(CreateUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user         


#모델 폼을 사용. 모델과 필드만 정해주면 자동으로 form이 작동
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        #fields = ('author', 'text',)
        fields = ['text']
        labels = {
            'text': '댓글쓰기',
        }
