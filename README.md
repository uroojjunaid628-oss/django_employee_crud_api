# Django Employee CRUD API

A REST API built with Django and Django REST Framework for managing employee records.

The API supports the complete CRUD workflow: creating, retrieving, updating, and deleting employee records. It uses SQLite for local data storage and Django REST Framework's browsable API for testing.

## Project Overview

This project focuses on building a simple backend API with Django REST Framework.

The application uses:

* Django models to define employee data
* Django REST Framework serializers to validate and convert data
* API views to handle HTTP requests
* URL routing to connect endpoints with views
* SQLite to store employee records

Each employee has a name, email, department, and salary. Email addresses are unique, so the same email cannot be registered for multiple employees.

## Features

* Create employee records
* Retrieve all employees
* Retrieve a single employee
* Update employee information
* Delete employee records
* Email uniqueness validation
* JSON request and response handling
* Django REST Framework browsable API
* SQLite database integration

## Tech Stack

* Python 3.10
* Django 5.2.15
* Django REST Framework 3.16.0
* SQLite
* Git & GitHub

## Employee Model

| Field        | Type    | Description                         |
| ------------ | ------- | ----------------------------------- |
| `id`         | Integer | Automatically generated primary key |
| `name`       | String  | Employee's name                     |
| `email`      | Email   | Unique employee email               |
| `department` | String  | Employee's department               |
| `salary`     | Integer | Employee's salary                   |

## API Endpoints

Base URL:

```text
http://127.0.0.1:8000/api/
```

| Method | Endpoint           | Description        |
| ------ | ------------------ | ------------------ |
| GET    | `/employees/`      | Get all employees  |
| POST   | `/employees/`      | Create an employee |
| GET    | `/employees/<id>/` | Get one employee   |
| PUT    | `/employees/<id>/` | Update an employee |
| DELETE | `/employees/<id>/` | Delete an employee |

## Example

### Create an Employee

**POST**

```text
/api/employees/
```

Request:

```json
{
    "name": "Hassan Khan",
    "email": "hassan@example.com",
    "department": "Software Development",
    "salary": 80000
}
```

Response:

```json
{
    "id": 6,
    "name": "Hassan Khan",
    "email": "hassan@example.com",
    "department": "Software Development",
    "salary": 80000
}
```

### Update an Employee

**PUT**

```text
/api/employees/6/
```

Request:

```json
{
    "name": "Hassan Khan Updated",
    "email": "hassan@example.com",
    "department": "AI Development",
    "salary": 90000
}
```

## Testing

The API was tested locally using Django REST Framework's browsable API.

The following operations were successfully tested:

* GET all employees
* POST a new employee
* GET a single employee
* PUT to update an employee
* DELETE an employee

Postman or another REST API client can also be used to test the endpoints.

## Project Structure

```text
django-employee-crud-api/
│
├── api/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── crud_project/
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   
│
├── .gitignore
├── manage.py
└── requirements.txt
└── README.md
```

## Running Locally

### 1. Clone the repository

```bash
git clone https://github.com/uroojjunaid628-oss/django-employee-crud-api.git
cd django-employee-crud-api
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

**macOS/Linux:**

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Apply migrations

```bash
python manage.py migrate
```

### 6. Start the development server

```bash
python manage.py runserver
```

The API will be available at:

```text
http://127.0.0.1:8000/api/employees/
```

## Future Improvements

* Add authentication and permissions
* Add pagination
* Add search and filtering
* Add automated API tests
* Add Swagger/OpenAPI documentation
* Use PostgreSQL for production
* Deploy the API to a cloud platform

## Author

**Urooj Junaid**

[GitHub](https://github.com/uroojjunaid628-oss)
