# Restapi-Task

This is a RESTful API built with Flask for managing beer store data. It provides endpoints to retrieve beer information, search for beers based on various parameters, and check the health of the database connection.

![Screenshot from 2023-06-03 01-17-27](https://github.com/arashafazeli/RestApi-Task/assets/90246599/75e1d6e1-a07f-4e71-9e62-98485ed5c906)

         
## Setup
1. Clone the repository: 
==git clone https://github.com/arashafazeli/RestApi-Task.git==
2. Navigate to the project directory:
- cd Restapi-Task
3. Create and activate a virtual environment:
- python3 -m venv venv
- source venv/bin/activate
4. Install the required dependencies:
- pip install -r requirements.txt
5. Start the Flask application:
- docker-compose up --build
6. Connet to database:
- docker exec -it < DATABASE CONTAINER NAME > bash
- psql -U < DATABASE USERNAME >

