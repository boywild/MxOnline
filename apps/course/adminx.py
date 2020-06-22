import xadmin
from .models import Course, CourseResource, Lesson, Video


class GlobalSetting(object):
    site_title = '暮雪'
    site_footer = '开科唯识'


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class CourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students']
    pass


class CourseResourceAdmin(object):
    pass


class LessonAdmin(object):
    pass


class VideoAdmin(object):
    pass


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)

xadmin.site.register(xadmin.views.CommAdminView, GlobalSetting)
xadmin.site.register(xadmin.views.BaseAdminView, BaseSetting)
