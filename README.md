# Simple App using Django REST framework


## Run App
python3 ./manage.py runserver


## Usage

* create new user (POST)
____
$ curl -X POST http://127.0.0.1:8000/user/create/ --data 'first_name=artem&last_name=artem&email=artem@mail.com&gender=Male&address=Yekaterinburg&username=fiskcom&dob=2020-05-30&phone=89520000000' | jq .
____
**Fields 'first_name', 'last_name', 'email', 'gender', 'address' are required.** *'email' field has to be unique!*


* view detail about user with id=14 (GET)
____
$ curl http://127.0.0.1:8000/users/14/detail/ | jq .
____


* update user info with id=14 (GET for view, PUT for change)
____
$ curl http://127.0.0.1:8000/users/14/update/ | jq .
____
$ curl -X PUT --data 'first_name=artem&last_name=artem&email=artem@gmail.com&username=fiscom&gender=Male&address=Yekaterinburg' http://127.0.0.1:8000/users/14/update/ | jq .
____
**Original email is required!**


* show users list (GET)
____
$ curl http://127.0.0.1:8000/users/list/ | jq .
____

* delete user with id=14 (GET)
____
$ curl http://127.0.0.1:8000/users/14/delete/ | jq .
___


## Date
2020-05-30
