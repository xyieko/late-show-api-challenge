## Late Show API
A RESTful API for managing guests, episodes, and appearances on a fictional Late Night Talk Show. Built using Flask, PostgreSQL, SQLAlchemy, JWT authentication, and tested with Postman.

##  Tech Stack
Python 3.12
Flask & Flask-RESTful
PostgreSQL
SQLAlchemy & Flask-Migrate
JWT Authentication (flask-jwt-extended)
Postman (for endpoint testing)
Dotenv (for secure environment config)

## Project Structure
late-show-api-challenge/ │ ├── server/ │ ├── app.py # App factory │ ├── config.py # Configuration settings │ ├── seed.py # Seeder script │ ├── models/ # SQLAlchemy models │ │ ├── guest.py │ │ ├── episode.py │ │ ├── appearance.py │ │ ├── user.py │ │ └── init.py │ ├── controllers/ # Blueprints / route logic │ │ ├── auth_controller.py │ │ ├── guest_controller.py │ │ ├── episode_controller.py │ │ ├── appearance_controller.py │ │ └── init.py │ ├── migrations/ # Alembic migration folder ├── challenge-4-lateshow.postman_collection.json ├── README.md └── .env

## Setup Instructions
1. Clone the repository
```
git clone https://github.com/your-username/late-show-api-challenge.git cd late-show-api-challenge
```
Set up a virtual environment 
```
python3 -m venv .venv source .venv/bin/activate
```
Install dependencies 
```
pip install -r requirements.txt
```
Configure environment Create a .env file: DATABASE_URI=postgresql://postgres:yourpassword@localhost:5432/lateshow_dev JWT_SECRET_KEY=super-secret

Run migrations 
```flask db init flask db migrate -m "Initial migration" flask db upgrade
```
Seed the database 
```
python -m server.seed
```
Start the server 
```
flask run
```
 ## Authentication
  Register a user: POST /auth/register

Login a user: POST /auth/login

Returns a JWT access token to be used on all protected routes via the Authorization: Bearer header.

## Postman Collection
 Import challenge-4-lateshow.postman_collection.json into Postman to test all endpoints.

## Sample Endpoints 
METHOD URL DESCRIPTION GET /guests List all guests POST /guests Create a new guest GET /episodes List all episodes POST /episodes Create a new episode POST /appearances Add guest appearance GET /appearances List all appearances

## Most routes are protected. You need a JWT token to access them.

## Testing Use Postman or curl to test the API.

Make sure to include the JWT in the headers when required.

## Contribution If you'd like to improve this project:

Fork it Create a new branch Submit a pull request