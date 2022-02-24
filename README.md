# Prices_of_Digital_Currencies

[![python](https://img.icons8.com/color/48/000000/python.png/)](https://www.python.org/)
[![django](https://img.icons8.com/color/48/000000/django.png)](https://www.djangoproject.com/)
[![DRF](https://img.icons8.com/color/48/000000/api.png)](https://www.django-rest-framework.org/)

#### Project Structure
---

```shell
└── Prices_of_Digital_Currencies
    ├── conf
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    │
    ├── prices
    │   ├── migrations
    │   │   └── __init__.py
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── serializers.py
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    │
    ├── manage.py
    ├── README.md
    └── requirements.txt
```

## Installation
---

First of all open the terminal or CMD and enter:

```shell
git clone https://github.com/mowbish/Prices_of_Digital_Currencies.git
```

After that go into the project folder and  create a virtual env


| Windows | Linux |
| --- | --- |
| ``> cd Prices_of_Digital_Currencies\  `` | ``$ cd Prices_of_Digital_Currencies/`` |
| ``> python -m venv venv `` | ``$ virtualenv venv`` |
| ``> venv\scripts\activate`` | ``$ source venv/bin/activate`` |

after activating venv now install requirements

```shell
pip install -r requirements.txt
```

Now enter this command:

```bash
python manage.py makemigrations
```

Now migrate all with this command:

```bash
python manage.py migrate
```

At the end you can run project with:

```bash
python manage.py runserver
```
### Also Rout's of project:

first of all go to the:

`http://127.0.0.1:8000/`

after that you can go to this rout's

+ `http://127.0.0.1:8000/`
+ `http://127.0.0.1:8000/signup`

Enjoy it ;)
