from django import forms
from captcha.fields import CaptchaField
import redis
from MxOnline.settings import REDIS_HOST, REDIS_PORT


class LoginForm(forms.Form):
    username = forms.CharField(required=True, min_length=2, max_length=20)
    password = forms.CharField(required=True, min_length=6, max_length=12)


class DynamicLoginForm(forms.Form):
    mobile = forms.CharField(required=True, min_length=11, max_length=11)
    captcha = CaptchaField()


class DynamicLoginPostForm(forms.Form):
    mobile = forms.CharField(required=True, min_length=11, max_length=11)
    code = forms.CharField(required=True, min_length=4, max_length=4)

    def clean(self):
        mobile = self.cleaned_data['mobile']
        code = self.cleaned_data['code']
        r = redis.Redis(REDIS_HOST, REDIS_PORT)
        redis_code = r.get(str(mobile))
        if code != redis_code:
            raise forms.ValidationError('验证码不正确')
        return self.cleaned_data
