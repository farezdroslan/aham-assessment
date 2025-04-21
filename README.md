# AHAM Fund Management System

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Setup Instructions](#setup-instructions)
3. [APIs](#apis)
   - [Endpoints](#endpoints)
   - [Sample Requests and Responses](#sample-requests-and-responses)
4. [SQL Database Schema](#sql-database-schema)

## Prerequisites
- Python 3.13.3
- Django 5.2
- Django REST Framework (DRF)
- PostgreSQL
- `psycopg2` (PostgreSQL adapter for Python)

## Setup Instructions

1. **Clone the repository:**

    ```bash
    git clone https://github.com/farezdroslan/aham-assessment.git
    cd aham-fund-management-system
    ```

2. **Create a virtual environment (Windows)**

    ```bash
    py -3 -m pip install pipenv
    ```

    ```bash
    py -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Set Up the Database**
    ```bash
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'fundapp',
            'USER': 'your_username',
            'PASSWORD': 'your_password',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    ```

4. **Apply Migrations**
    ```bash
    py manage.py makemigrations
    py manage.py migrate
    ```

5. **Run the development server**
    ```markdown
    py manage.py runserver
    ```

6. **Access the API**
    ```bash
    http://127.0.0.1:8000/fundapp/ 
    ```


## APIs

### Endpoints

Example:
```markdown
### Endpoints

| Endpoint                        | Method | Description                                  |
|---------------------------------|--------|----------------------------------------------|
| `/fundapp/funds/`               | GET    | Retrieve all funds                           |
| `/fundapp/funds/create/`        | POST   | Create a new fund                            |
| `/fundapp/funds/<id>/`          | GET    | Retrieve a specific fund by ID               |
| `/fundapp/funds/<id>/`          | PUT    | Update a specific fund by ID                 |
| `/fundapp/funds/<id>/`          | DELETE | Delete a specific fund by ID                 |
```

## Sample Requests and Responses

1. **Retrieve all funds**

    **Request**


    GET [http://127.0.0.1:8000/fundapp/funds/]


    **Response**

    ```json
    [
        {
            "fund_id": 1,
            "fund_name": "Tech Growth Fund",
            "fund_manager": 1,
            "fund_description": "A fund focused on tech startups.",
            "nav": "100.50",
            "performance": "5.25"
        }
    ]
    ```

2. **Create a New Fund**

    **Request**

    POST [http://127.0.0.1:8000/fundapp/funds/create]
    Content-Type: application/json

    ```json
    {
        "fund_name": "New Fund",
        "fund_manager": 1,
        "fund_description": "A new fund description.",
        "nav": "200.75",
        "performance": "6.50"
    }
    ```

    **Response**

    ```json
    {
        "fund_id": 2,
        "fund_name": "New Fund",
        "fund_manager": 1,
        "fund_description": "A new fund description.",
        "nav": "200.75",
        "performance": "6.50"
    }
    ```

3. **Update a Fund**

    **Request**

    PUT [http://127.0.0.1:8000/fundapp/funds/1] 
    Content-Type: application/json

    ```json
    {
        "fund_name": "Updated Fund Name",
        "fund_manager": 1,
        "fund_description": "Updated fund description.",
        "nav": "300.00",
        "performance": "7.00"
    }
    ```

    **Response**
    ```json
    {
        "fund_id": 1,
        "fund_name": "Updated Fund Name",
        "fund_manager": 1,
        "fund_description": "Updated fund description.",
        "nav": "300.00",
        "performance": "7.00"
    }
    ```

4. **Delete a Fund**

    **Request**
    DELETE [http://127.0.0.1:8000/fundapp/funds/1] 

    **Response**
    ```json
    {
        "message": "Fund deleted successfully."
    }
    ```

## SQL Database Schema

1. **Manager Table**

    ```sql
    CREATE TABLE manager (
        manager_id SERIAL PRIMARY KEY,
        manager_name VARCHAR(255) NOT NULL,
        manager_bio TEXT
    );
    ```

2. **Fund Table**
    ```sql
    CREATE TABLE fund (
        fund_id SERIAL PRIMARY KEY,
        fund_name VARCHAR(255) UNIQUE NOT NULL,
        fund_manager INTEGER REFERENCES manager(manager_id) ON DELETE CASCADE,
        fund_description TEXT NOT NULL,
        nav NUMERIC(10, 2) NOT NULL CHECK (nav >= 0.01),
        performance NUMERIC(5, 2) NOT NULL CHECK (performance BETWEEN -100 AND 100),
        date_of_creation DATE DEFAULT CURRENT_DATE
    );
    ```

3. **Investor Table**
    ```sql
    CREATE TABLE investor (
        investor_id SERIAL PRIMARY KEY,
        investor_name VARCHAR(255) NOT NULL,
        investor_email VARCHAR(255) UNIQUE NOT NULL
    );
    ```

4. **Investment Table**
    ```sql
    CREATE TABLE investment (
        investment_id SERIAL PRIMARY KEY,
        investor_id INTEGER REFERENCES investor(investor_id) ON DELETE CASCADE,
        fund_id INTEGER REFERENCES fund(fund_id) ON DELETE CASCADE,
        investment_amount NUMERIC(10, 2) NOT NULL CHECK (investment_amount > 0),
        investment_date DATE DEFAULT CURRENT_DATE
    );
    ```



