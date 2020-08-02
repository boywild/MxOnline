from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt
from apps.organization.views import OrgView, AddAskView

urlpatterns = [
    url(r'^list/$', OrgView.as_view(), name='list'),
    url(r'^add_ask/$', AddAskView.as_view(), name='add_ask')
]
