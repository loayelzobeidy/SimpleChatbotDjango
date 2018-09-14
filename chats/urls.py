from . import views
from django.conf.urls import url


urlpatterns = [
url('insert_questions',views.insert_questions_json,name='insert_questions'),    
url('insert_answers',views.insert_possible_Answers_json,name='insert_answers'),    
url('message',views.chat,name='message'),
url('questions',views.get_questions,name='questions'),
url('answers',views.insert_answers,name='answers'),
url('user/(?P<username>\w{0,50})/$',views.getUser,name='user'),



]