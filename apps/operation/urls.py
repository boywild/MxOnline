from django.conf.urls import url
from apps.organization.views import AddFavView

urlpatterns = [
    url(r'^add_fav/$', AddFavView.as_view(), name='add_fav')
]