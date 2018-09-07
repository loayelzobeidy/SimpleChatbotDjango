from django.contrib import admin
from .models import Category,Question,PossibleAnswer
admin.site.register(Question)
admin.site.register(Category)
admin.site.register(PossibleAnswer)
# Register your models here.
