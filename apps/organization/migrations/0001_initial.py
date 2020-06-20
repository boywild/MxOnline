# Generated by Django 3.0.6 on 2020-06-20 15:58

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('name', models.CharField(max_length=20, verbose_name='城市名')),
                ('desc', models.CharField(default='', max_length=200, verbose_name='描述')),
            ],
            options={
                'verbose_name': '城市',
                'verbose_name_plural': '城市',
            },
        ),
        migrations.CreateModel(
            name='CourseOrg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('name', models.CharField(max_length=200, verbose_name='机构名')),
                ('desc', models.TextField(verbose_name='机构介绍')),
                ('tag', models.CharField(max_length=10, verbose_name='机构标签')),
                ('category', models.CharField(choices=[('pxjg', '培训机构'), ('gr', '个人'), ('gx', '高校')], default='pxjg', max_length=200, verbose_name='类别')),
                ('click_nums', models.PositiveIntegerField(default=0, verbose_name='浏览次数')),
                ('fav_nums', models.PositiveIntegerField(default=0, verbose_name='收藏次数')),
                ('image', models.ImageField(upload_to='org/%Y/%m', verbose_name='机构logo')),
                ('address', models.CharField(max_length=150, verbose_name='机构地址')),
                ('students', models.PositiveIntegerField(default=0, verbose_name='学习人数')),
                ('courses_nums', models.PositiveIntegerField(default=0, verbose_name='课程数')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.City', verbose_name='城市')),
            ],
            options={
                'verbose_name': '机构',
                'verbose_name_plural': '机构',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('name', models.CharField(max_length=200, verbose_name='名字')),
                ('work_years', models.CharField(max_length=200, verbose_name='工作年限')),
                ('work_company', models.CharField(max_length=200, verbose_name='就只公司')),
                ('work_position', models.CharField(max_length=200, verbose_name='工作职位')),
                ('points', models.CharField(max_length=200, verbose_name='教学特点')),
                ('click_nums', models.CharField(max_length=200, verbose_name='浏览次数')),
                ('fav_nums', models.CharField(max_length=200, verbose_name='收藏次数')),
                ('age', models.CharField(max_length=200, verbose_name='年龄')),
                ('image', models.ImageField(upload_to='teacher/%Y/%m', verbose_name='图像')),
                ('course_org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.CourseOrg', verbose_name='机构')),
            ],
            options={
                'verbose_name': '教师',
                'verbose_name_plural': '教师',
            },
        ),
    ]
