from django.shortcuts import render
from django.views.generic import View
from pure_pagination import Paginator, PageNotAnInteger
from apps.course.models import Course
from apps.operation.models import UserFavorite


# Create your views here.

class CourseListView(View):
    def get(self, request):
        all_courses = Course.objects.all()
        hot_courses = Course.objects.order_by('-click_nums')[:3]
        sort = request.GET.get('sort', '')

        # 筛选
        if sort == 'hot':
            all_courses = all_courses.order_by('-click_nums')
        elif sort == 'students':
            all_courses = all_courses.order_by('-students')

        # 课程分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_courses, per_page=10, request=request)
        courses = p.page(page)
        return render(request, 'course-list.html', {
            'all_courses': courses,
            'hot_courses': hot_courses,
            'sort': sort
        })


class CourseDetailView(View):
    def get(self, request, course_id, *args, **kwargs):
        course = Course.objects.get(id=course_id)
        is_fav_teacher = UserFavorite.objects.filter(user_id=request.user, fav_type=3, fav_id=course.teacher.id)
        is_fav_org = UserFavorite.objects.filter(user_id=request.user, fav_type=2, fav_id=course.course_org.id)
        return render(request, 'course-detail.html', {
            'course': course,
            'is_fav_teacher': is_fav_teacher,
            'is_fav_org': is_fav_org
        })


class CourseLessonView(View):
    def get(self, request, course_id, *args, **kwargs):
        return render(request, 'course-video.html')
