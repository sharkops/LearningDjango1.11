from django.shortcuts import render, HttpResponse

# Create your views here.
from django import forms
from captcha.fields import CaptchaField
from django.contrib.auth.hashers import make_password

class CaptchaTestForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(min_length=6)
    captcha = CaptchaField(error_messages={
        "invalid": "验证码错误"
    })



def some_view(request):
    if request.POST:
        register_form = CaptchaTestForm(request.POST)

        if register_form.is_valid():
            user_name = register_form.cleaned_data.get('email')
            password = register_form.cleaned_data.get('password')
            print(user_name, password)
            password = make_password(password)
            from users.models import UserProfile
            UserProfile.objects.create(**{"username": user_name,
                                          "email": user_name,
                                          "password": password})
            return HttpResponse("注册成功")
    else:
        register_form = CaptchaTestForm()

        return render(request, 'register.html', locals())
