from django.db import models
from apps.user.models import BaseModel
from apps.course.models import Course
from apps.user.models import UserProfile
from six import python_2_unicode_compatible


# Create your models here.

@python_2_unicode_compatible
class UserAsk(BaseModel):
    name = models.CharField(verbose_name='名字', max_length=20)
    mobile = models.CharField(verbose_name='联系电话', max_length=11)
    course_name = models.CharField(verbose_name='课程名', max_length=50)

    class Meta:
        verbose_name = '课程咨询'
        verbose_name_plural = verbose_name


@python_2_unicode_compatible
class CourseComment(BaseModel):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='用户')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='课程')
    comments = models.CharField(verbose_name='评论', max_length=200)

    class Meta:
        verbose_name = '课程留言'
        verbose_name_plural = verbose_name


@python_2_unicode_compatible
class UserCourse(BaseModel):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='用户')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='课程')

    class Meta:
        verbose_name = '用户课程'
        verbose_name_plural = verbose_name


@python_2_unicode_compatible
class UserFavorite(BaseModel):
    TYPE_CHOICE = (
        (1, '课程'),
        (2, '课程机构'),
        (3, '教师')
    )
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='用户')
    fav_id = models.PositiveIntegerField(verbose_name='收藏id', blank=True, null=True)
    fav_type = models.PositiveIntegerField(verbose_name='收藏类型', choices=TYPE_CHOICE, default=1)

    class Meta:
        verbose_name = '我的收藏'
        verbose_name_plural = verbose_name


@python_2_unicode_compatible
class UserMessage(BaseModel):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='用户')
    message = models.CharField(verbose_name='消息内容', max_length=200)
    has_read = models.BooleanField(verbose_name='是否已读', default=False)

    class Meta:
        verbose_name = '我的消息'
        verbose_name_plural = verbose_name
