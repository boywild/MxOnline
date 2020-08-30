from django.db import models
from apps.user.models import BaseModel
from apps.organization.models import CourseOrg, Teacher
from DjangoUeditor.models import UEditorField
from six import python_2_unicode_compatible

# Create your models here.

@python_2_unicode_compatible
class Course(BaseModel):
    DEGREE_CHOICE = (
        ('cj', '初级'),
        ('zj', '中级'),
        ('gj', '高级')
    )
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='课程所属教师')
    course_org = models.ForeignKey(CourseOrg, on_delete=models.CASCADE, verbose_name='课程所属机构')
    name = models.CharField(verbose_name='课程名', max_length=50)
    desc = models.CharField(verbose_name='描述', max_length=300)
    learn_times = models.PositiveIntegerField(verbose_name='时长/分', default=0)
    degree = models.CharField(verbose_name='难度', choices=DEGREE_CHOICE, max_length=2)
    students = models.PositiveIntegerField(verbose_name='学习次数', default=0)
    fav_nums = models.PositiveIntegerField(verbose_name='收藏次数', default=0)
    click_nums = models.PositiveIntegerField(verbose_name='点击数', default=0)
    notice = models.CharField(verbose_name='课程公告', max_length=300, default='')
    category = models.CharField(verbose_name='类别', max_length=20, default=u'后端开发')
    tag = models.CharField(verbose_name='标签', max_length=10, default='')
    youneed_know = models.CharField(verbose_name='课程须知', max_length=300, default='')
    teacher_tell = models.CharField(verbose_name='老师告诉你', max_length=300, default='')
    is_classics = models.BooleanField(verbose_name='是否经典', default=False)
    detail = UEditorField(u'课程详情', width=600, height=300, toolbars='full', imagePath='courses/ueditor/images/',
                          filePath='courses/ueditor/files/',
                          upload_settings={'imageMaxSize': 1204000}, settings={}, command=None, blank=True, default='')
    image = models.ImageField(verbose_name='封面图', upload_to='courses/%Y/%m', max_length=100)
    is_banner = models.BooleanField(verbose_name='是否广告位', default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '课程'
        verbose_name_plural = verbose_name

    def lesson_nums(self):
        return self.lesson_set.all().count()

@python_2_unicode_compatible
class Lesson(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='课程')
    name = models.CharField(verbose_name='章节', max_length=100)
    learn_times = models.PositiveIntegerField(verbose_name='章节时长/分', default=0)

    class Meta:
        verbose_name = '课程章节'
        verbose_name_plural = verbose_name

@python_2_unicode_compatible
class Video(BaseModel):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='课程')
    name = models.CharField(verbose_name='视频名', max_length=100)
    learn_times = models.PositiveIntegerField(verbose_name='视频时长/分', default=0)
    url = models.CharField(verbose_name='视频链接', max_length=1000)

    class Meta:
        verbose_name = '课程视频'
        verbose_name_plural = verbose_name

@python_2_unicode_compatible
class CourseResource(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='课程')
    name = models.CharField(verbose_name='资源名', max_length=100)
    file = models.FileField(verbose_name='资源文件', upload_to='courses/resourse/%Y/%m', max_length=200)

    class Meta:
        verbose_name = '课程资源'
        verbose_name_plural = verbose_name
