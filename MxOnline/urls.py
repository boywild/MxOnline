"""MxOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.views.static import serve
from MxOnline.settings import MEDIA_ROOT
from apps.user.views import LoginView, LogoutView, RegisterView, SendSmsView, DynamicLoginView, UserCenterView, \
    UserCenterMyCourseView, UserCenterMyMessageView

import xadmin

xadmin.autodiscover()

# version模块自动注册需要版本控制的 Model
from xadmin.plugins import xversion

xversion.register_models()

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name="index"),
    path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    path('ueditor/', include('DjangoUeditor.urls')),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    path('login/', LoginView.as_view(), name="login"),
    path('d_login/', DynamicLoginView.as_view(), name="d_login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('register/', RegisterView.as_view(), name="register"),
    path('send_sms/', csrf_exempt(SendSmsView.as_view()), name="send_sms"),
    url(r'^org/', include(('apps.organization.urls', 'organizations'), namespace='org')),
    url(r'^op/', include(('apps.operation.urls', 'operation'), namespace='op')),
    url(r'^course/', include(('apps.course.urls', 'course'), namespace='course')),
    url(r'^users/', include(('apps.user.urls', 'users'), namespace='users'))
]
