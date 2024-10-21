from django.contrib.admin import ModelAdmin, register

from illallangi.data.education.models import Course


@register(Course)
class CourseModelAdmin(ModelAdmin):
    pass
