from django.contrib import admin

# Register your models here.
from .models import City, CourseOrg, Teacher


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass


@admin.register(CourseOrg)
class CourseOrgAdmin(admin.ModelAdmin):
    pass


@admin.register(Teacher)
class Teacherdmin(admin.ModelAdmin):
    pass
