import csv
import json
with open('/home/loay/Work/chatbotHm/cities.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    data =[]
    for row in csv_reader:
        data.append({"pk":line_count,"fields":{"question_id":"1",
         "answer":row[0]+","+row[1]},"model": "questions.PossibleAnswer"})
        line_count+=1
    print(data)
    with open('/home/loay/Work/chatbotHm/dataCity.json', 'w') as outfile:
        json_list = json.dump(data,outfile)
        print(json_list)