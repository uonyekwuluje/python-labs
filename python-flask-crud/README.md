# Flask PostgreSQL CRUD Application

A complete CRUD application using:

- Python
- Flask
- PostgreSQL
- SQLAlchemy
- Flask-Migrate
- HTML
- CSS
- Vanilla JavaScript

## Features

- Create products
- List products
- Get a single product
- Update products
- Delete products
- PostgreSQL database
- REST API
- Responsive frontend
- Database migrations

---

## Requirements

Install the following:

- Python 3.11+
- PostgreSQL 14+
- pip

---

# Create PostgreSQL Database

```
CREATE DATABASE pyappdb;
CREATE USER app_user WITH PASSWORD 'password1';
GRANT ALL PRIVILEGES ON DATABASE pyappdb TO app_user;
GRANT ALL ON SCHEMA public TO app_user;
ALTER DATABASE pyappdb OWNER TO app_user;
```

# Run The Service
pip install -r requirements.txt
```
docker build -t flask-crud:latest .

docker run -d \
  --name flask-crud \
  -p 5000:5000 \
  -e DATABASE_URL="postgresql+psycopg://app_user:password1@localhost:5432/pyappdb" \
  flask-crud:latest
```

# Test Link
curl http://localhost:5000

# API 
```
The REST API is:

Method	    Endpoint	      Operation
GET	        /api/items	      List items
GET	        /api/items/1	  Get item
POST	    /api/items	      Create item
PUT	        /api/items/1	  Update item
DELETE	    /api/items/1	  Delete item
GET	        /health	Health    check
```
