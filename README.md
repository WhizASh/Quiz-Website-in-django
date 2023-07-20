# Quiz-Website-in-django
A Basic quiz website made in django

#### SETUP

1. Run  `python manage.py makemigrations` in the termimal
2. Run `python manage.py migrate `
3. Run `python manage.py runserver` to Start the server

### Features 
* Custom Question Mode
* Random question mode

### How it works 

It fetches random question from [open trivia db](https://opentdb.com/) and just displays it on to the html page . 

The custom question mode will store the question and options in the database and the test id wil be generated for the current questions added , this test id can be used to access the current batch of questions added . 


