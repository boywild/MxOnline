from django.conf.urls import url
from apps.course.views import CourseListView

urlpatterns = [
    url(r'^list/', CourseListView.as_view(), name='list')
]
