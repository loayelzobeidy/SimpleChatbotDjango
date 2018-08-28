# -*- coding: utf-8 -*-

import json
from django.shortcuts import render
from chats.models import  User,Skill,Title
# Create your views here.
from questions.models import Question
from django.http import HttpResponse
from django.forms.models import model_to_dict
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
    # if request.method != 'GET':
    #     print('exceptionn')
    #     return
    dictionaries = Question.objects.all().order_by('category') 
    print(dictionaries,' nowww')    
    return HttpResponse(json.dumps({"data": dictionaries}), content_type='application/json')    
    # return HttpResponse(json_stuff, content_type ="application/json")

def chat(request):
    index  = int(request.COOKIES.get('index', '0') )    
    if request.method != 'POST' and not index==0:
        print('exceptionn')
        return  HttpResponse(json.dumps({"message":"Should be a post request"}), content_type ="application/json")
    dictionaries =  Question.objects.all()
    #  [ Question.as_dict() for Question in]
    print(dictionaries) 
    body_unicode = request.body
    body = json.loads(body_unicode)
    users = User.objects.filter(email=body['email'])
    if(not len(users)==0 and (index==1)):
        return  HttpResponse(json.dumps({"message":"user exist"}), content_type ="application/json")
    index  = index % len(dictionaries)
    print("index===>>",index)    
    email = body['email']
    name = body['name']
    print(User.objects.filter(email=email),"userssss")
    if(index==3):
        skills = body['skills']
        u = User(email=email)
        u.employed = False
        u.years_of_experience = 0
        for skill in skills:
           sk = Skill(skill=skill)
           sk.save()
           u.save()
           u.skills.add(sk)
        print(u,"usersss==>>>")
        u.save()
    if(index==4):
        employed = body['employed']
        u = User(email=email)
        u.years_of_experience = 0
        u.employed = employed
        u.save()
    print(User.objects.filter(email=email),"userssss")    
    question = dictionaries[index].question
    if(index==7):
        titles = body['titles']
        u = User(email=email)
        for title in titles:
           sk = Title(title=title)
           sk.save()
           u.save()
           u.skills.add(sk)
        print(u,"usersss==>>>")
    if(index==6):
        years_of_experience = body['experience']
        u = User(email=email)
        u.years_of_experience = years_of_experience
        u.save()
    if(index==5):
        job_title = body['current_title']
        u = User(email=email)
        u.job_title = job_title
        u.save()
        print(u,"usersss==>>>")
    if(index==4 and u.employed==False):
        index +=2
    if(question[0]==','):
        question = 'Hi '+name+' '+dictionaries[index].question
    if(question[len(question)-1]==','):
        question = dictionaries[index].question+' '+name
    response  = HttpResponse(json.dumps(question), content_type ="application/json")
    print("question",dictionaries[index])
    response.set_cookie('index', index + 1 )
    return response
