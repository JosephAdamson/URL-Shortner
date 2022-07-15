# URL shortener project made with django.

## Demo
---

- https://urlshortener9891.herokuapp.com/

<img src="https://i.imgur.com/3eygg4z.png" height=500 widht=500>

## Run Locally
---
- Download source files
- either in your virtual enviroment or locally install the necessary requirements
  ```
  pip3 install -r requirements.txt
  ```
- generate your own secret key for the project; in the project root execute:
    ```
    echo "SECRET_KEY=$(head -c 32 /dev/urandom | base64)" > .env
    ```
- set up and start the app using Django:
    ```
    python manage.py makemirgrations
    python manage.py migrate
    python manage.py runserver
    ```

## Stack
 ``` 
 - Python
 - Django
 - HTML
 - CSS
 - Heroku
 ```