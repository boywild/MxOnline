from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from apps.operation.forms import UserFavForm
from apps.course.models import Course
from apps.organization.models import CourseOrg, Teacher
from apps.operation.models import UserFavorite


# Create your views here.


class AddFavView(View):
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return JsonResponse({
                'status': 'fail',
                'msg': '用户未登录'
            })
        user_fav_form = UserFavForm(request.POST)
        if user_fav_form.is_valid():
            fav_id = user_fav_form.cleaned_data['fav_id']
            fav_type = user_fav_form.cleaned_data['fav_type']

            existed_records = UserFavorite.objects.filter(user=request.user, fav_id=fav_id, fav_type=fav_type)
            # 已收藏
            if existed_records:
                existed_records.delete()
                # 课程
                if fav_type == 1:
                    course = Course.objects.get(id=fav_id)
                    course.fav_nums -= 1
                    course.save()
                # 课程机构
                elif fav_type == 2:
                    course_org = CourseOrg.objects.get(id=fav_id)
                    course_org.fav_nums -= 1
                    course_org.save()
                # 教师
                elif fav_type == 3:
                    teacher = Teacher.objects.get(id=fav_id)
                    teacher.fav_nums -= 1
                    teacher.save()

                return JsonResponse({
                    'status': 'success',
                    'msg': '收藏'
                })
            # 未收藏
            else:
                user_fav = UserFavorite()
                user_fav.fav_type = fav_type
                user_fav.fav_id = fav_id
                user_fav.user = request.user
                user_fav.save()

                return JsonResponse({
                    "status": "success",
                    "msg": "已收藏"
                })
        else:
            return JsonResponse({
                'status': 'fail',
                'msg': '参数错误'
            })
