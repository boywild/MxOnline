from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from MxOnline.settings import API_KEY_YUN_PIAN, REDIS_HOST, REDIS_PORT
import json
import redis
from apps.user.forms import LoginForm, DynamicLoginForm, DynamicLoginPostForm, RegisterGetForm, RegisterPostForm
from apps.user.models import UserProfile
from utils.YunPian import single_send_sms
from utils.random_str import generate_random


# Create your views here.

class LoginView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('index'))

        login_form = DynamicLoginForm()
        return render(request, 'login.html', {
            'login_form': login_form
        })

    def post(self, request, *args, **kwargs):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return render(request, 'login.html', {'msg': '用户名或密码错误', 'login_form': login_form})
        else:
            return render(request, 'login.html', {'login_form': login_form})


class SendSmsView(View):
    def post(self, request, *args, **kwargs):
        send_sms_form = DynamicLoginForm(request.POST)
        re_dict = {}
        if send_sms_form.is_valid():
            mobile = send_sms_form.cleaned_data['mobile']
            code = generate_random(4, 0)
            res_sms = single_send_sms(API_KEY_YUN_PIAN, code, mobile)
            if res_sms['code'] == 0:
                re_dict['status'] = 'SUCCESS'
                r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0, charset="utf8", decode_responses=True)
                r.set(str(mobile), code)
                r.expire(str(mobile), 60 * 5)
            else:
                re_dict['msg'] = res_sms['msg']
        else:
            for key, value in send_sms_form.errors.items():
                re_dict[key] = value[0]

        return JsonResponse(re_dict)


class DynamicLoginView(View):

    def post(self, request, *args, **kwargs):
        login_form = DynamicLoginPostForm(request.POST)
        is_dynamic = True
        if login_form.is_valid():
            mobile = login_form.cleaned_data['mobile']
            existed_users = UserProfile.objects.filter(mobile=mobile)
            if existed_users:
                user = existed_users[0]
            else:
                user = UserProfile(username=mobile)
                user.mobile = mobile
                password = generate_random(10, 2)
                user.set_password(password)
                user.save()
            login(request, user)
            next = request.GET.get('next', '')
            if next:
                return HttpResponseRedirect(next)
            return HttpResponseRedirect(reverse('index'))
        else:
            d_login = DynamicLoginForm
            return render(request, 'login.html', {
                'login_form': login_form,
                'd_login': d_login,
                'is_dynamic': is_dynamic
            })


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse('index'))

    def post(self, request, *args, **kwargs):
        pass


class RegisterView(View):
    def get(self, request, *args, **kwargs):
        register_form = RegisterGetForm(request.GET)
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('index'))
        return render(request, 'register.html', {
            'register_form': register_form
        })

    def post(self, request, *args, **kwargs):
        register_post_form = RegisterPostForm(request.POST)
        if register_post_form.is_valid():
            mobile = register_post_form.cleaned_data['mobile']
            password = register_post_form.cleaned_data['password']

            user = UserProfile(mobile=mobile)
            user.username = mobile
            user.mobile = mobile
            user.set_password(password)
            user.save()
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            register_get_form = RegisterGetForm()
            return render(request, 'register.html', {
                'register_post_form': register_post_form,
                'register_get_form': register_get_form
            })
