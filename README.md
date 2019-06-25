# favorite-things
Britecore-app


[![Coverage Status](https://coveralls.io/repos/github/matthewacha/favorite-things/badge.svg?branch=master)](https://coveralls.io/github/matthewacha/favorite-things?branch=master)
[![Build Status](https://travis-ci.org/matthewacha/favorite-things.svg?branch=master)](https://travis-ci.org/matthewacha/favorite-things)
[![Maintainability](https://api.codeclimate.com/v1/badges/90ae425e8edb1b1cdb95/maintainability)](https://codeclimate.com/github/matthewacha/favorite-things/maintainability)


## About

Favorite-things is an API that enables you to keep track of all you favorite things. It is hosted at ['https://favorite-things-back.herokuapp.com']('https://favorite-things-back.herokuapp.com')

## Technologies
- Python 3
- Django Rest Framework
- PostgreSQL
- Docker
- docker-compose

The [front-end service ](https://github.com/matthewacha/favorite-things-front) is built using the [Vue](https://www.django-rest-framework.org/). Hosted on heroku [https://favorite-things-front.herokuapp.com/v1/](https://favorite-things-front.herokuapp.com/v1/)


## Project setup

Ensure to install the above `technologies` listed before you start.

### Clone repository

```
$ git clone https://github.com/matthewacha/favorite-things.git
$ cd favorite-things
```

### Setup virtualenv

```
$ virtualenv -p python3 venv
$ source venv/bin/activate
```

### Setup environment variables

For Mac
```
export PORT=<database port> DB_HOST=<database host> DB_PASSWORD=<database passord> DB_USER=<database user> DB_NAME=<databse name>
```

### Install dependencies

```
pip3 install -r requirements.txt
```

### Apply migrations

```
$ python3 manage.py migrate
```

### Run the server

```
$ python3 manage.py runserver
```

### To run tests

```
$ python3 manage.py test
```

#### with coverage

```
$ coverage run --source='.' ./manage.py test
```
## Documentation on usage of the API
Documentation for the usage of the API endpoints can be found at [http://127.0.0.1:8000/docs/](http://127.0.0.1:8000/docs/) when running a local server.