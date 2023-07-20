from django.shortcuts import render,redirect
import requests,random,json
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import question,userProfiles
from django.contrib import messages

# Create your views here.

def index(request):
     return render(request,'Main/index.html')

def Home(request):
     return render(request,'Main/Home.html')

# current_question = 0

def project(request):
     return render(request,'Main/project.html')

def infinity_play(request):
        # if request.method=='POST':
        #      current_question+=1
        #      if

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

                q = json.dumps(q)  
                return render(request,'Main/infinity_play.html',{'q':q})
        else:
              return HttpResponse("Error: {} {}".format( response.status_code, response.text))

encrypted_string=''

def custom_question_game(request):
        # questions = question.objects.all()       #go to the question adding page 
        no1 = int(encrypted_string[:3])
        no2 = int(encrypted_string[3:])
        questions = question.objects.filter(id__range=(no1, no2+1))
        # print(decrypted_number1, decrypted_number2)  
        i=0
        qs={}
        for q in questions:
             opt = []
             opt.append(q.option1)  
             opt.append(q.option2)  
             opt.append(q.option3)  
             opt.append(q.option4)
             qs.update({i:{'question':q.question,'options':opt,'answer':q.answer}})
             i=i+1

        qs = json.dumps(qs) 
        return render(request,'Main/custom_question_game.html',{'q':qs})


api_url=''

def Topics(request):
        response = requests.get(api_url)
        x=response.json()
        q={}
        if response.status_code == requests.codes.ok and x['response_code']==0:
                for i in range(0,10):
                        options = list(x['results'][0]['incorrect_answers'])
                        options.append(x['results'][0]['correct_answer'])
                        options = random.sample(options,len(options))           #Shuffle all the options with incorrect and correct answers
                        question = x['results'][0]['question']                  # store the question in question variable 
                        ans = x['results'][0]['correct_answer']                 # store the answer in ans variable

                        q={'question':question,'options':options,'answer':ans}  # store all variables in q dictionary 
                        
                q = json.dumps(q)
                return render(request,'Main/Topics.html',{'q':q})
                
        else:
            return HttpResponse("Error: {} {}".format( response.status_code, response.text))
        

def Topics_selection(request):
       global api_url
       if request.method=='POST':
            id=request.POST.get('trivia_category')
            dif = request.POST.get('trivia_difficulty')
            api_url = 'https://opentdb.com/api.php?amount=10'
            if dif=='any'and id=='any':
                api_url=(api_url)
            elif dif=='any':
                api_url=(api_url+'&category={}'+'&type=multiple'.format(id))
            elif id=='any':
                  api_url=(api_url+'&difficulty={}'+'&type=multiple'.format(dif))
            else:
                api_url=(api_url+'&category={}&difficulty={}'+'&type=multiple'.format(id,dif))
            
            return redirect('Topics')
       else:
            return render(request,'Main/Topics-selection.html')



def custom_questions(request):
      global encrypted_string
      if request.method=='POST':
        encrypted_string = request.POST.get('Code')
        # questions = question.objects.all()       #go to the question adding page 
        # return render(request,'Main/custom_question_game.html',{'qs':qs})
        return redirect('custom_question_game')
      else:
        return render(request,"Main/custom_questions.html")       # go to the login page not login 
      


def login(request):
      if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            #redirect to the next page
            return redirect('Home')
        else:
            return redirect('login')
      else:
            return render(request,'Main/login.html')
      
def register(request):
      if request.method=='POST':
        username= request.POST.get('username')
        password = request.POST.get('password1')
        # password2 = request.POST.get('password2')
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")

        if password != '':
            try:
                User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                return redirect('login')
            except:
                return HttpResponse("some error occured in usename or stuff")
        else:
            return redirect('register')
      else:
        return render(request,'Main/register.html')

s_id=0

def add_question(request):
     global s_id
     s_id=question.objects.latest('id').id
     if request.method == 'POST':
        questions = request.POST.get('question')
        option1 = request.POST.get('option1')
        option2 = request.POST.get('option2')
        option3 = request.POST.get('option3')
        option4 = request.POST.get('option4')
        answer = request.POST.get('answer')

        # Check for empty values
        if not all([questions, option1, option2, option3, option4, answer]):
            messages.error(request, 'Please fill in all fields.')
            return redirect('add_question')  # Redirect back to the form page

        
        if answer not in [option1, option2, option3, option4]:
            messages.error(request, 'Answer must be one of the provided options.')
            return redirect('add_question')  # Redirect back to the form page

        
        question.objects.create(question=questions,option1=option1,option2=option2,option3=option3,option4=option4,answer=answer)
        
        return redirect('question_success')
     else:
        return render(request, 'Main/add_question.html')
               

def Test_id(request):
        global encrypted_string
        last_id = question.objects.latest('id').id
        encrypted_string = str(s_id).zfill(3) + str(last_id).zfill(3)
        # print(encrypted_string)  
        # name=User.objects.get('username')
        # userProfiles.objects.create(usernname=name,test_id=encrypted_string)
        return render(request,'Main/test_id.html',{'q':encrypted_string})
        
def question_success(request):
     return render(request,'Main/question_success.html')

# decrypted_number1 = int(encrypted_string[:3])
# decrypted_number2 = int(encrypted_string[3:])
# print(decrypted_number1, decrypted_number2)  