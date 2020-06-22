import xadmin
from .models import UserAsk, CourseComment, UserCourse, UserFavorite, UserMessage


class UserAskAdmin(object):
    pass


class CourseCommentAdmin(object):
    pass


class UserCourseAdmin(object):
    pass


class UserFavoriteAdmin(object):
    pass


class UserMessageAdmin(object):
    pass


xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(CourseComment, CourseCommentAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
