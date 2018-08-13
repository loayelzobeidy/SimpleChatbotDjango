from . import views
from django.conf.urls import url


urlpatterns = [
url('',views.get_questions,name='home'),
url('/message',views.chat,name='message')


]