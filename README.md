# Restapi-Task

This is a RESTful API built with Flask for managing beer store data. It provides endpoints to retrieve beer information, search for beers based on various parameters, and check the health of the database connection.

         
    ______________________Docker-compose________________________
    |     ____________                       _____________     |
         |            |    | Dockerfile |   |             |    |_______
 GET-----| FLASK-APP  |=====================|  POSTGRESQL |    |       |   
 POST    |            |                     |             |====|SQLFILE|
 HEALTH  |____________|                     |_____________|    |_______|
                |                                  |
                |                                  | 
             Postman(Endpoint test)             Tableplus(database dashboard)
## Setup
1. Clone the repository: 
git clone https://github.com/arashafazeli/RestApi-Task.git
2. Navigate to the project directory:
cd Restapi-Task
3. Create and activate a virtual environment:
python3 -m venv venv
source venv/bin/activate
4. Install the required dependencies:
pip install -r requirements.txt
5. Start the Flask application:
docker-compose up --build

