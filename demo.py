import requests
import random
api_url = 'https://opentdb.com/api.php?amount=10&type=multiple'
response = requests.get(api_url)
x=response.json()
q={}
if response.status_code == requests.codes.ok:
                for i in range(0,10):
                  options = list(x['results'][i]['incorrect_answers'])
                  options.append(x['results'][i]['correct_answer'])
                  options = random.sample(options,len(options))           #Shuffle all the options with incorrect and correct answers
                  question = x['results'][i]['question']                  # store the question in question variable 
                  ans = x['results'][i]['correct_answer']                 # store the answer in ans variable
                  category = x['results'][i]['category']
                  q.update({i:{'question':question,'options':options,'answer':ans,'category':category}} ) # store all variables in q dictionary 


        # print(q[i]['question'])
        # print(q[i]['options'][0])
        # print(q[i]['options'][1])
        # print(q[i]['options'][2])
        # print(q[i]['answer'])
        # print(q[i]['category'])
        # print("-"*30)
        # print(q[i])
print(len(q))