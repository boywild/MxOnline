# Generated by Django 3.0.6 on 2020-06-20 22:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0003_auto_20200620_1724'),
        ('course', '0003_auto_20200620_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_org',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.CourseOrg', verbose_name='课程所属机构'),
        ),
        migrations.AlterField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.Teacher', verbose_name='课程所属教师'),
        ),
    ]