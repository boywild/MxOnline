# Generated by Django 3.0.6 on 2020-08-30 21:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_auto_20200620_2232'),
        ('operation', '0004_auto_20200806_1138'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usercourse',
            options={'verbose_name': '用户课程', 'verbose_name_plural': '用户课程'},
        ),
        migrations.RemoveField(
            model_name='usercourse',
            name='fav_id',
        ),
        migrations.RemoveField(
            model_name='usercourse',
            name='fav_type',
        ),
        migrations.AddField(
            model_name='usercourse',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='course.Course', verbose_name='课程'),
        ),
    ]
