from django.contrib import admin

# Register your models here.
from .models import UserAsk, CourseComment, UserCourse, UserFavorite, UserMessage


@admin.register(UserAsk)
class UserAskAdmin(admin.ModelAdmin):
    pass


@admin.register(CourseComment)
class CourseCommentAdmin(admin.ModelAdmin):
    pass


@admin.register(UserCourse)
class UserCoursedmin(admin.ModelAdmin):
    pass


@admin.register(UserFavorite)
class UserFavoriteAdmin(admin.ModelAdmin):
    pass


@admin.register(UserMessage)
class UserMessageAdmin(admin.ModelAdmin):
    pass
