from django.conf.urls import url
from django.urls import path
from apps.user.views import UserCenterView, UserCenterMyMessageView, UserCenterMyCourseView, UserCenterMyFavCourseiew, \
    UserCenterMyFavOrgView, UserCenterMyFavTeacherView

urlpatterns = [
    path('info/', UserCenterView.as_view(), name="info"),
    path('course/', UserCenterMyCourseView.as_view(), name="mycourse"),
    path('fav_course/', UserCenterMyFavCourseiew.as_view(), name="myfav_course"),
    path('fav_teacher/', UserCenterMyFavTeacherView.as_view(), name="myfav_teacher"),
    path('fav_org/', UserCenterMyFavOrgView.as_view(), name="myfav_org"),
    path('message/', UserCenterMyMessageView.as_view(), name="mymessage"),
]
