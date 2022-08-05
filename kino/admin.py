from django.contrib import admin
from .models import *
from embed_video.admin import AdminVideoMixin


admin.site.register(Session)
admin.site.register(News)


class video(AdminVideoMixin, admin.ModelAdmin):
    pass


admin.site.register(Film)

#  myvenv\Scripts\activate

#  py manage.py runserver