from . import views
from django.conf.urls import url


urlpatterns = [
url('insert_questions',views.insert_questions,name='insert_questions'),    
url('message',views.chat,name='message'),
url('questions',views.get_questions,name='questions'),

]