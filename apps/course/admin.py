from django.contrib import admin

# Register your models here.
from .models import Course, CourseResource, Lesson, Video


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    pass


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    pass


@admin.register(CourseResource)
class CourseResourceAdmin(admin.ModelAdmin):
    pass
