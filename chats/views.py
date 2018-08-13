# -*- coding: utf-8 -*-
from django.views.decorators.csrf import csrf_exempt
from __future__ import unicode_literals
import json
from django.shortcuts import render
from chats.models import Question, User
# Create your views here.
from django.http import HttpResponse


def get_questions(request):
    if request.method != 'GET':
        print('exceptionn')
        return
    all_users =Question.objects.all()
    print(all_users)
    json_stuff = json.dumps({"list_of_questions" :list( all_users)})    
    return HttpResponse(json_stuff, content_type ="application/json")
@csrf_exempt
def chat(request):
    if request.method != 'POST':
        print('exceptionn')
        return
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    email = body['email']
    print(email,"emailll===>>")
