from django import forms
from captcha.fields import CaptchaField
import redis
from MxOnline.settings import REDIS_HOST, REDIS_PORT
from apps.user.models import UserProfile


class LoginForm(forms.Form):
    username = forms.CharField(required=True, min_length=2, max_length=20)
    password = forms.CharField(required=True, min_length=6, max_length=12)


class DynamicLoginForm(forms.Form):
    mobile = forms.CharField(required=True, min_length=11, max_length=11)
    captcha = CaptchaField()


class DynamicLoginPostForm(forms.Form):
    mobile = forms.CharField(required=True, min_length=11, max_length=11)
    code = forms.CharField(required=True, min_length=4, max_length=4)

    def clean_code(self):
        mobile = self.data.get('mobile')
        code = self.data.get('code')
        r = redis.Redis(REDIS_HOST, REDIS_PORT)
        redis_code = r.get(str(mobile))
        if code != redis_code:
            raise forms.ValidationError('验证码不正确')
        return code


class RegisterGetForm(forms.Form):
    mobile = forms.CharField(required=True, min_length=11, max_length=11)
    captcha = CaptchaField()


class RegisterPostForm(forms.Form):
    mobile = forms.CharField(required=True, min_length=11, max_length=11)
    code = forms.CharField(required=True, min_length=4, max_length=4)
    password = forms.CharField(required=True, min_length=6, max_length=12)

    def clean_mobile(self):
        mobile = self.data.get('mobile')
        user = UserProfile.objects.filter(mobile=mobile)
        if user:
            raise forms.ValidationError('该手机号码已注册')
        return mobile

    def clean_code(self):
        mobile = self.data.get('mobile')
        code = self.data.get('code')
        r = redis.Redis(REDIS_HOST, REDIS_PORT, db=0, charset="utf8", decode_responses=True)
        redis_code = r.get(str(mobile))
        if code != redis_code:
            raise forms.ValidationError('验证码不正确')
        return code

