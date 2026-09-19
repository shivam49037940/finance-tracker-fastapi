# authentication
    User
        Register
        Login
        Profile

# Finance Management

    User
        income add
        expense add
        transaction view
        transaction delete

Authentication Endpoint

    POST /auth/register
    POST /auth/login
    GET /auth/me

Transaction Endpoint

    POST /transactions
    GET /transactions
    DELETE /trsnactions/{transaction_id}

    GET /transaction/analytics/monthly
    GET/transactions/analytics/categories
    GET/transactions/analytics/top-category

# Installation

pip install fastapi,uvicorn
pip install sqlalchemy
pip3 install "passlib[bcrypt]" bcrypt==3.2.0
pip3 install python-jose