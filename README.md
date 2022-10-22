# Articles

A simple CRUD API with Django and DjangoRestFramework

## Deployed Url in Heroku

('https://articles-web-api.herokuapp.com/articles')

## To run Locally

- Clone the Project Repository ('https://github.com/Popoola-Sinaayo/Articles.git')

- Download Python ('https://www.python.org/downloads/')

- Install and Add Python to environment path

- Run 'python -m venv env'

- For Windows run 'env\Scripts\activate'

- For Mac run 'env\Scripts\activate'

- Run 'pip install -r requirements.txt'

- Run 'python manage.py makemigrations Management'

- Run 'python manage.py migrate'

- Run 'python manage.py runserver'

## Documentation

The following HttpRequest are Valid to the '/articles' endpoint

- GET [loads all articles]

- POST [create a new article]

- PUT [Update an article]

- DELETE [Delete an article]

An article has four fields

- title [Mandatory]
- content [Mandatory]
- creator [Mandatory]
- comment [Optional]
- id [Added automatically by default, no need to specify]

To get all created articles

- Get Request to the '/articles' endpoint

**To create a new Article**

- Post Request to the '/articles' endpoint in JSON format with the fields[title, content, creator, comment(Optional)]

**To Update an Article**

- PUT request to the '/articles' enpoint in JSON format update can be done by pasing either the id or title as part of the request body accompanied with the fields to be changes

**To Delete an Article**

- DELETE request to the '/articles' endpoint in JSON format, pass only the Article id or title, not both
