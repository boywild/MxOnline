from django.db import models
from apps.user.models import BaseModel


# Create your models here.

class Course(BaseModel):
    DEGREE_CHOICE = (
        ('cj', '初级'),
        ('zj', '中级'),
        ('gj', '高级')
    )
    name = models.CharField(verbose_name='课程名', max_length=50)
    desc = models.CharField(verbose_name='描述', max_length=300)
    learn_times = models.PositiveIntegerField(verbose_name='时长/分', default=0)
    degree = models.CharField(verbose_name='难度', choices=DEGREE_CHOICE, max_length=2)
    students = models.PositiveIntegerField(verbose_name='学习次数', default=0)
    fav_nums = models.PositiveIntegerField(verbose_name='收藏次数', default=0)
    click_nums = models.PositiveIntegerField(verbose_name='点击数', default=0)
    notice = models.CharField(verbose_name='课程公告', max_length=300, default='')
    category = models.CharField(verbose_name='类别', max_length=20)
    tag = models.CharField(verbose_name='标签', max_length=10)
    youneed_know = models.CharField(verbose_name='课程须知', max_length=300)
    teacher_tell = models.CharField(verbose_name='老师告诉你', max_length=300)
    detail = models.TextField(verbose_name='课程详情')
    image = models.ImageField(verbose_name='封面图', upload_to='courses/%Y/%m', max_length=100)

    class Meta:
        verbose_name = '课程'
        verbose_name_plural = verbose_name


class Lesson(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='课程')
    name = models.CharField(verbose_name='章节', max_length=100)
    learn_times = models.PositiveIntegerField(verbose_name='章节时长/分', default=0)

    class Meta:
        verbose_name = '课程章节'
        verbose_name_plural = verbose_name


class Video(BaseModel):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='课程')
    name = models.CharField(verbose_name='视频名', max_length=100)
    learn_times = models.PositiveIntegerField(verbose_name='视频时长/分', default=0)
    url = models.CharField(verbose_name='视频链接', max_length=1000)

    class Meta:
        verbose_name = '课程视频'
        verbose_name_plural = verbose_name


class CourseResource(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='课程')
    name = models.CharField(verbose_name='资源名', max_length=100)
    file = models.FileField(verbose_name='资源文件', upload_to='courses/resourse/%Y/%m', max_length=200)

    class Meta:
        verbose_name = '课程资源'
        verbose_name_plural = verbose_name
