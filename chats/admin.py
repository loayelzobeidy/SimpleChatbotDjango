
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib import admin

from .models import Answer,Title,User,Session

admin.site.register(Answer)
admin.site.register(Title)
admin.site.register(User)
admin.site.register(Session)

# Register your models here.
