from django.db import models
from apps.user.models import BaseModel
from DjangoUeditor.models import UEditorField


# Create your models here.
class City(BaseModel):
    name = models.CharField(verbose_name='城市名', max_length=20)
    desc = models.CharField(verbose_name='描述', max_length=200, default='')

    class Meta:
        verbose_name = '城市'
        verbose_name_plural = verbose_name


class CourseOrg(BaseModel):
    CATEGORY_CHOICE = (
        ('pxjg', '培训机构'),
        ('gr', '个人'),
        ('gx', '高校'),
    )
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='城市')
    name = models.CharField(verbose_name='机构名', max_length=200)
    desc = UEditorField(u'机构介绍', width=600, height=300, toolbars='full', imagePath='course/ueditor/iamges/',
                        filePath='course/ueditor/images/',
                        upload_settings={'imageMaxSize': 1204000}, settings={}, command=None, blank=True)
    tag = models.CharField(verbose_name='机构标签', max_length=10)
    category = models.CharField(verbose_name='类别', choices=CATEGORY_CHOICE, max_length=200, default='pxjg')
    click_nums = models.PositiveIntegerField(verbose_name='浏览次数', default=0)
    fav_nums = models.PositiveIntegerField(verbose_name='收藏次数', default=0)
    image = models.ImageField(verbose_name='机构logo', upload_to='org/%Y/%m', max_length=100)
    address = models.CharField(verbose_name='机构地址', max_length=150)
    students = models.PositiveIntegerField(verbose_name='学习人数', default=0)
    courses_nums = models.PositiveIntegerField(verbose_name='课程数', default=0)

    class Meta:
        verbose_name = '机构'
        verbose_name_plural = verbose_name


class Teacher(BaseModel):
    course_org = models.ForeignKey(CourseOrg, on_delete=models.CASCADE, verbose_name='机构')
    name = models.CharField(verbose_name='名字', max_length=200)
    work_years = models.CharField(verbose_name='工作年限', max_length=200)
    work_company = models.CharField(verbose_name='就只公司', max_length=200)
    work_position = models.CharField(verbose_name='工作职位', max_length=200)
    points = models.CharField(verbose_name='教学特点', max_length=200)
    click_nums = models.CharField(verbose_name='浏览次数', max_length=200)
    fav_nums = models.CharField(verbose_name='收藏次数', max_length=200)
    age = models.CharField(verbose_name='年龄', max_length=200)
    image = models.ImageField(verbose_name='图像', upload_to='teacher/%Y/%m', max_length=100)

    class Meta:
        verbose_name = '教师'
        verbose_name_plural = verbose_name
