# -*- coding: utf-8 -*-

import json
from django.shortcuts import render
from chats.models import Question, User
# Create your views here.
from django.http import HttpResponse

def insert_questions(request):
    if request.method != 'POST':
        print('exceptionn')
        return
    body_unicode = request.body
    body = json.loads(body_unicode)
    questions = body['questions']    
    for question in questions:
        q = Question(question=question['question'])
        q.save()
    return HttpResponse(request.body, content_type ="application/json")
    
    
def get_questions(request):
    if request.method != 'GET':
        print('exceptionn')
        return
    dictionaries = [ Question.as_dict() for Question in Question.objects.all() ]
    return HttpResponse(json.dumps({"data": dictionaries}), content_type='application/json')    
    # return HttpResponse(json_stuff, content_type ="application/json")

def chat(request):
    if request.method != 'POST':
        print('exceptionn')
        return
    dictionaries = [ Question.as_dict() for Question in Question.objects.all()]
    index  = int(request.COOKIES.get('index', '0') )
    index  = index % len(dictionaries)
    print("index===>>",index)    
    body_unicode = request.body
    body = json.loads(body_unicode)
    email = body['email']
    name = body['name']
    print(User.objects.filter(email=email),"userssss")
    if(index==1):
        skills = body['skills']
        u = User(email=email,name=name,employed=False,years_of_experience=0)
        u.save()
    question = dictionaries[index]
    if(question[0]==','):
        question = 'Hi '+name+' '+dictionaries[index]
    if(question[len(question)-1]==','):
        question = dictionaries[index]+' '+name
    
    response  = HttpResponse(json.dumps(question), content_type ="application/json")
    print("question",dictionaries[index])
    response.set_cookie('index', index + 1 )
    return response
