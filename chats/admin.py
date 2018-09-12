
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib import admin

from .models import Answer,Title,User,Session,Skill,Switch_reasons

admin.site.register(Answer)
admin.site.register(Title)
admin.site.register(User)
admin.site.register(Session)
admin.site.register(Skill)
admin.site.register(Switch_reasons)


# Register your models here.
