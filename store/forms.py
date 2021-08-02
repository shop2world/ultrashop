from django import forms
from .models import Product
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class CreateUserForm(UserCreationForm): # 내장 회원가입 폼을 상속받아서 확장한다.
    email = forms.EmailField(required=True) # 이메일 필드 추가

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True): # save 오버라이딩
        user = super(CreateUserForm, self).save(commit=False) # 기존 id와 비번 저장. save(commit=False)는 중복 저장 방지
        user.email = self.cleaned_data["email"]
        if commit:
            user.save() #저장
        return user