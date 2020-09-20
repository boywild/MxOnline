from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from pure_pagination import Paginator, PageNotAnInteger
from apps.course.models import Course, Video, CourseTag, CourseResource
from apps.operation.models import UserFavorite, UserCourse


# Create your views here.

class CourseListView(View):
    def get(self, request):
        all_courses = Course.objects.order_by('-add_time')
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
    '''
    课程详情
    '''

    def get(self, request, course_id, *args, **kwargs):
        course = Course.objects.get(id=int(course_id))

        is_fav_teacher = False
        is_fav_org = False
        if request.user.is_authenticated:
            if UserFavorite.objects.filter(user_id=request.user, fav_type=3, fav_id=course.teacher.id):
                is_fav_teacher = True
            if UserFavorite.objects.filter(user_id=request.user, fav_type=2, fav_id=course.course_org.id):
                is_fav_org = True

        tags = course.coursetag_set.all()
        tag_list = [tag.tag for tag in tags]
        related_courses = set()
        course_tags = CourseTag.objects.filter(tag__in=tag_list).exclude(course__id=course.id)
        print(course_tags)
        for course_tag in course_tags:
            related_courses.add(course_tag.course)

        print(related_courses)
        return render(request, 'course-detail.html', {
            'course': course,
            'is_fav_teacher': is_fav_teacher,
            'is_fav_org': is_fav_org
        })


class CourseLessonView(View):
    '''
    学习课程
    '''

    def get(self, request, course_id, *args, **kwargs):
        course_detail = Course.objects.get(id=course_id)
        # 课程浏览量+1
        course_detail.click_nums += 1
        course_detail.save()
        course_resources = CourseResource.objects.filter(course=course_detail)

        if request.user.is_authenticated:
            # 查询是否已经学习过该课程
            user_course = UserCourse.objects.filter(user=request.user, course=course_detail)
            if not user_course:
                user_course = UserCourse(user=request.user, course=course_detail)
                user_course.save()

                course_detail.students += 1
                course_detail.save()

            user_courses = UserCourse.objects.filter(course=course_detail)
            user_ids = [user_course.user.id for user_course in user_courses]
            all_courses = UserCourse.objects.filter(user_id__in=user_ids).exclude(course=course_detail).order_by(
                '-course__click_nums')[:5]
            related_courses = []
            for item in all_courses:
                related_courses.append(item.course)
        else:
            return HttpResponseRedirect(reverse('login'))

        return render(request, 'course-video.html', {
            'course_detail': course_detail,
            'course_resources': course_resources,
            'related_courses': related_courses
        })


class CourseVideoView(View):
    def get(self, request, course_id, video_id, *args, **kwargs):
        course_detail = Course.objects.get(id=course_id)
        video = Video.objects.get(id=video_id)
        return render(request, 'course-play.html', {
            'course_detail': course_detail,
            'video': video
        })


class CourseCommentView(View):
    def get(self, request, course_id):
        return render(request, 'course-comment.html')
