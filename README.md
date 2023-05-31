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

1) Copy this project on your local machine `git clone ссылка на мой гитхаб`
2) Write in a terminal this command `docker-compose up --build -d`
3) Open an application, which can send **GET/POST/PUT/PATCH/DELETE** methods, f.e `Postman` and write in the browse page this address `http://localhost/`
4) Write your request and push "SEND" button
5) Receive a response in `JSON` format from the application

---

### Examples:

#### Request: GET http://localhost/notes

#### Response:

```json
[
    {
        "id": 1, 
        "name": "Note 1", 
        "text": "Hello world!"
    }, 
    {
        "id": 2, 
        "name": "Note 2", 
        "text": "Code your way to success"
    }, 
    {
        "id": 3, 
        "name": "Note 3", 
        "text": "Test"
    }
]
```

#### Request: GET http://localhost/notes/2

#### Response:

```json
{
    "id": 2, 
    "name": "Note 2", 
    "text": "Code your way to success"
}
```

#### Request: POST http://localhost/notes

```json
{
    "name": "Note 4", 
    "text": "New note"
}
```

#### Response:

```json
{
    "id": 4,
    "name": "Note 4", 
    "text": "New note"
}
```

#### Request: PUT http://localhost/notes/3

```json
{
    "name": "Updated note", 
    "text": "Updated text"
}
```

#### Response: 

```json
{
    "id": 3,
    "name": "Updated note", 
    "text": "Updated text"
}
```

#### Request: DELETE http://localhost/notes/2

#### Response:

```json
{
    "message": "Note has deleted successfully"
}
```
