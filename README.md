# Django API Server

Simple starter built with Python / Django Rest / Sqlite3 and JWT Auth. The authentication flow is built with [json web tokens](https://jwt.io).

<br />

> Features:

- Authentication with JWT (login, logout, register)
- APIs to get candidate details, all candidate, create candidates and update candidates

## ✨ How to use the code

> **Step #1** -  Clone the sources

```bash
$ git clone https://github.com/joetho786/Jobapplication-Reviewer-Backend.git
$ cd <to directory containing manage.py>
```

<br />

> **Step #2** - Create a virtual environment

```bash
$ # Virtualenv modules installation (Unix based systems)
$ virtualenv env
$ source env/bin/activate
$
$ # Virtualenv modules installation (Windows based systems)
$ # virtualenv env
$ # .\env\Scripts\activate
```

<br />

> **Step #3** - Install dependencies using PIP

```bash
$ pip install -r requirements.txt
```

<br />

> **Step #4** - Start the API server

```bash
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```

The API server will start using the default port `8000`.

<br />

## ✨ API

For a fast set up, use this POSTMAN file: [api_sample](https://github.com/app-generator/api-server-Django/blob/master/media/api.postman_collection.json)

> **Register** - `api/users/signup`

```
POST api/users/signup
Content-Type: application/json

{
    "username":"test",
    "password":"pass", 
    "email":"test@appseed.us"
}
```

<br />

> **Login** - `api/users/login`

```
POST /api/users/login
Content-Type: application/json

{
    "password":"pass", 
    "email":"test@appseed.us"
}
```

<br />

> **Logout** - `api/users/logout`

```
POST api/users/logout
Content-Type: application/json
authorization: JWT_TOKEN (returned by Login request)

{
    "token":"JWT_TOKEN"
}
```

> **Get Candidates** - `api/candidate`

```
GET api/candidate
Response:
[
   {
        "id": 1,
        "created_at": "24-05-2022|09:45:23",
        "name": "XYZ",
        "education": "Test College",
        "experience": "",
        "website": "",
        "description": "",
        "email": "<email address>",
        "phone": "<phone number>",
        "address": "<address>",
        "city": "<city>",
        "state": "<state>",
        "zipcode": "<zipcode>",
        "country": "<country>",
        "projects": "<project details>",
        "resume": "<resume url>",
        "updated_at": "2022-05-24T09:49:49.225964Z",
        "status": "Applied"
    }
]

```


> Create Candidate - `api/candidate`

```
POST api/candidate
Content-Type: application/json
payload schema:
{
        "id": 1,
        "created_at": "24-05-2022|09:45:23",
        "name": "XYZ",
        "education": "Test College",
        "experience": "",
        "website": "",
        "description": "",
        "email": "<email address>",
        "phone": "<phone number>",
        "address": "<address>",
        "city": "<city>",
        "state": "<state>",
        "zipcode": "<zipcode>",
        "country": "<country>",
        "projects": "<project details>",
        "resume": "<resume url>",
        "updated_at": "2022-05-24T09:49:49.225964Z",
        "status": "Applied"
    }
```
