# -*- coding: utf-8 -*-

import json
import ast
from django.core import serializers
from django.shortcuts import render
from chats.models import  User,Skill,Title,Session,Answer,Switch_reasons
# Create your views here.
from questions.models import Question,PossibleAnswer,Category
from django.http import HttpResponse
from django.forms.models import model_to_dict
import uuid
def insert_questions_json(request):
    with open('/home/loay/Work/chatbotHm/questions.json') as f:
        data = json.load(f)
        index  = 0
        for question in data:
            print(index)
            index = index+1
            category = Category.objects.filter(category_id=question["fields"]["category"])[0]
            question = Question(question_id = uuid.uuid4(),question=question["fields"]["question"],answerType=question["fields"]["answerType"],category=category,priority=question["fields"]["priority"])
            question.save()
    return HttpResponse("questions inserted successfully")  
def getUser(request, username):
    user = [ User.as_dict() for User in User.objects.filter(email=username) ]
    dummy = Skill.objects.all()
    skills = User.objects.filter(email=username)[0].switch_reasons
    print(skills,'skilllsss')
    print(dummy,'sks')
    
    print(user,'userrerrrr')
    return HttpResponse(user, content_type ="application/json")    
def insert_possible_Answers_json(request):
    with open('/home/loay/Work/chatbotHm/possibleAnswers.json') as f:
        data = json.load(f)
        index  = 0
        for possible in data:
            print(index,possible["fields"]["question_id"])
            index = index+1
            question = Question.objects.filter(question_id=possible["fields"]["question_id"])
            if(len(question)>0):
                question=question[0]
                possibleAnswer = PossibleAnswer(answer_id= uuid.uuid4(),question_id=question,answer=possible["fields"]["answer"])
                possibleAnswer.save()
    return HttpResponse("answers inserted successfully")    
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
def insert_answers(request):
    if request.method != 'POST':
        print('exceptionn')
        return
    body_unicode = request.body
    body = json.loads(body_unicode)
    user_id = body['email']    
    user = User.objects.filter(email=user_id)
    if(len(user)==0):
        user = User(email=user_id)
        user.save()
    else :
        user = user[0]
    session = Session.objects.filter(user_id=user)
    if(len(session)>0):
        questions = Question.objects.all().order_by('category','priority')
        print(questions )
        user_session = session[0]
        if 'answer' not in body:
             return HttpResponse("answer filed doesn't exsist in the request")
        answer =  body['answer'] 
        # if(user_session.index_question==0):
        #     print('heeereeree')
        #     user.name = body['answer']
        #     user.save()        
        question_id =  questions[user_session.index_question]
        possibleAnswer = Answer(answer_id=uuid.uuid4(),user_id = user,question_id=question_id,answer=answer)
        possibleAnswer.save()
        message = "answer saved"
    else:
        session = Session(user_id=user,index_category=0,index_question=0)
        session.save()
        message = "new user created"
    print(user_session.index_question,"indexxx")
    if(questions[user_session.index_question].answerType=="Select"):
        attributes = body["answer"].split(',')
       
            # attribute = globals()[questions[user_session.index_question].className]
            # print(attribute,"A")
            # attribute_temp = attribute(attr)
            # attribute_temp.save()
        listIWantToStore = ast.literal_eval(getattr(user,questions[user_session.index_question].owner))
        print("list ",listIWantToStore,type(attributes))
        if(listIWantToStore==None):
            listIWantToStore=[]
        print(type(listIWantToStore),"List",questions[user_session.index_question].owner)
        listIWantToStore +=attributes
        setattr(user,questions[user_session.index_question].owner,json.dumps(listIWantToStore))
        user.save()
        print(listIWantToStore,"B")
        # attribute_user = getattr(user,questions[user_session.index_question].owner)
        # attribute_user.add(attribute_temp)
        # user.save()
    else:
        print("innnn==>>",questions[user_session.index_question])
        setattr(user,questions[user_session.index_question].owner,body['answer']) 
        print(user.name)  
        user.save()   
    if(user_session.index_question<len(questions)-1):
            user_session.index_question = user_session.index_question+1
            user_session.save()  
    return HttpResponse(message)

def get_questions(request):
    # if request.method != 'GET':
    #     print('exceptionn')
    #     return
    # with open('/home/loay/Work/chatbotHm/questions.json', 'r') as f:
    #      data = json.load(f)
    # print(data)
    # for deserialized_object in serializers.deserialize("json", data):
    #     deserialized_object.save()
    # data = serializers.serialize("json", Question.objects.all())    
    dictionaries = [ Question.as_dict() for Question in Question.objects.all().order_by('category','priority') ]
    print(dictionaries,' nowww')    
    return HttpResponse(json.dumps({"data": dictionaries}), content_type='application/json')    
    # return HttpResponse(json_stuff, content_type ="application/json")

def chat(request):
    if request.method != 'POST':
        print('exceptionn')
        return  HttpResponse(json.dumps({"message":"Should be a post request"}), content_type ="application/json")
    dictionaries = [ Question.as_dict() for Question in Question.objects.all().order_by('category','priority') ]
    query = Question.objects.all().order_by('category','priority')
    body_unicode = request.body
    body = json.loads(body_unicode)
    user_id = body['email']  
    user = User.objects.filter(email=user_id)
    
    if(len(user)==0):
        user = User(email=user_id,name=body['name'])
        user.save()
        session = Session(user_id=user,index_question=0,index_category=0)
        session.save()     
    else :
        user = user[0]
        session = Session.objects.filter(user_id=user)[0]
        # print("replace",dictionaries[session.index_question]["question"])
        if(session.index_question>=len(query)):
            return  HttpResponse(json.dumps({"message":"Questions has ended"}), content_type ="application/json")
        dictionaries[session.index_question]["question"]=dictionaries[session.index_question]["question"].replace("#Name",user.name)        
    # print(PossibleAnswer.objects.filter(question_id=query[session.index_question]))
    while(session.index_question<len(query)):
       if(session.index_question>=len(query)):
            return  HttpResponse(json.dumps({"message":"Questions has ended"}), content_type ="application/json")
       flag = True
       after = query[session.index_question].after
       if(after==None):
           after = '{}'
       after = json.loads(after)
       for attribute,value  in after.items():
           if(not(getattr(user,attribute)==value)):
               flag = False
               break
       if(not flag):
            session.index_question += 1
            session.save()
       else :
            break
    if(session.index_question>=len(query)):
            return  HttpResponse(json.dumps({"message":"Questions has ended"}), content_type ="application/json")     
    possibleAnswers  = [ possibleAnswer.as_dict() for possibleAnswer in PossibleAnswer.objects.filter(question_id=query[session.index_question])]
    # print(dictionaries[session.index_question],possibleAnswers)
    #  [ Question.as_dict() for Question in]
    return HttpResponse(json.dumps({"data":dictionaries[session.index_question],"possibleanswers":possibleAnswers}), content_type='application/json')
