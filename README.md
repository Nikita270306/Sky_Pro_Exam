# SkyPro 

## Exam at the end of second semester

---

### About project:

- It is simple application on `Flask` with based `API`
- Application runs from `Docker` container 

---

### Requirements:

```python
psycopg2-binary==2.9.6
aniso8601==9.0.1
attrs==23.1.0
blinker==1.6.2
click==8.1.3
Flask==2.3.2
flask-restx==1.1.0
Flask-SQLAlchemy==3.0.3
itsdangerous==2.1.2
Jinja2==3.1.2
jsonschema==4.17.3
MarkupSafe==2.1.2
marshmallow==3.19.0
packaging==23.1
pyrsistent==0.19.3
pytz==2023.3
SQLAlchemy==2.0.15
typing_extensions==4.6.2
Werkzeug==2.3.4
```

---

### How to use:


---

1) Copy this project on your local machine `git clone https://github.com/Nikita270306/Sky_Pro_Exam.git`
2) Write in a terminal this command `docker-compose up --build -d`
3) Open an application, which can send **GET/POST/PUT/PATCH/DELETE** methods, f.e `Postman` and write in the browse page this address `http://localhost/schedule`
4) Write your request and push "SEND" button
5) Receive a response in `JSON` format from the application

---

### Examples:

#### Request: GET http://localhost/schedule

#### Response:

```json
[
    {
        "cabinet": 403,
        "id": 1,
        "teacher": "Gosha",
        "date": "2023:06:02:10:30:00",
        "lesson": "Programming"
    }, 
    {
        "cabinet": 404,
        "id": 2,
        "teacher": "Ivan",
        "date": "2023:06:02:12:00:00",
        "lesson": "Math"
    }, 
    {
        "cabinet": 403,
        "id": 3,
        "teacher": "Zhenya",
        "date": "2023:06:02:15:00:00",
        "lesson": "Psychology"
    }
]
```

#### Request: GET http://localhost/schedule/2

#### Response:

```json
{
        "cabinet": 404,
        "id": 2,
        "teacher": "Ivan",
        "date": "2023:06:02:12:00:00",
        "lesson": "Math"
    }
```

#### Request: POST http://localhost/schedule

```json
{
    "lesson": "test-lesson",
    "date": "test-date",
    "teacher": "test-teacher",
    "cabinet": "666"
}
```

#### Response:

```json
{
    "cabinet": 666,
    "id": 4,
    "teacher": "test-teacher",
    "date": "test-date",
    "lesson": "test-lesson"
}
```

#### Request: PUT http://localhost/schedule/3

```json
{
    "lesson": "updated-lesson",
    "date": "updated-date",
    "teacher": "updated-teacher",
    "cabinet": "555"
}
```

#### Response: 

```json
{
    "cabinet": 555,
    "id": 1,
    "teacher": "updated-teacher",
    "date": "updated-date",
    "lesson": "updated-lesson"
}
```

#### Request: PATCH http://localhost/schedule/3

```json
{
    "lesson": "updated-lesson",
    "date": "updated-date"
}
```

#### Response: 

```json
{
    "cabinet": 403,
    "id": 3,
    "teacher": "Ivan",
    "date": "updated-date",
    "lesson": "updated-lesson"
}
```

#### Request: DELETE http://localhost/schedule/2

#### Response:

```json
{
    "message": "lesson has deleted successfully"
}
```
