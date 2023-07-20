
from django.urls import path,include
from .views import Home,infinity_play,Topics_selection,Topics,login,register,custom_questions,add_question,Test_id,custom_question_game,question_success,index,project
urlpatterns = [
    path('',index,name="index"),
    path('Home/',Home,name="Home"),
    path('infinity_play/',infinity_play,name="infinity_play"),
    path('Topics-selection/',Topics_selection,name="Topics-selection"),
    path('Topics/',Topics,name='Topics'),
    path('project/', project, name='project'),
    path('login/',login,name="login"),
    path('register',register,name="register"),
    path('custom_questions',custom_questions,name="custom_questions"),
    path('add_question',add_question,name="add_question"),
    path('Test_id',Test_id,name="Test_id"),
    path('custom_question_game',custom_question_game,name="custom_question_game"),
    path('question_success/',question_success,name="question_success"),
    # path('congratulations/', congratulations_page, name='congratulations'),



    
]