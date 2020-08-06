# Generated by Django 3.0.6 on 2020-08-06 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0003_auto_20200620_1724'),
    ]

    operations = [
        migrations.AddField(
            model_name='userfavorite',
            name='fav_id',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='收藏id'),
        ),
        migrations.AddField(
            model_name='userfavorite',
            name='fav_type',
            field=models.PositiveIntegerField(choices=[(1, '课程'), (2, '课程机构'), (3, '教师')], default=1, verbose_name='收藏类型'),
        ),
    ]
