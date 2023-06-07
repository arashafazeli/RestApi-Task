# Restapi-Task

This is a RESTful API built with Flask for managing beer store data. It provides endpoints to retrieve beer information, search for beers based on various parameters, and check the health of the database connection.

![Screenshot from 2023-06-03 01-17-27](https://github.com/arashafazeli/RestApi-Task/assets/90246599/c138c75d-871b-4d11-b7ef-2059df97c13a)

         
## Setup
1. Clone the repository: 
    - git clone https://github.com/arashafazeli/RestApi-Task.git
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
    - SELECT * FROM < DATABASE NAME >;

# metrics to monitor for this specific service:

## Response Time:
 Measure the time taken by the service to respond to requests. This metric helps evaluate the service's performance and identify potential bottlenecks.

## Error Rate:
 Monitor the rate of errors or failed requests. This metric indicates the service's reliability and can help identify issues that need attention.

## Request Rate:
 Track the number of requests the service receives over time. This metric helps understand the service's load and capacity requirements.

## Database Connection Status:
 Monitor the health of the database connection to ensure the service can successfully connect and interact with the database.

## HTTP Status Codes:
 Monitor the distribution of HTTP status codes returned by the service. This metric helps identify any abnormal or unexpected responses.

## Endpoint Availability:
 Track the availability of critical endpoints. This metric ensures that the service is accessible and functioning correctly.

## CPU and Memory Usage:
 Monitor the resource utilization of the service, including CPU and memory usage. This metric helps identify potential performance issues or resource constraints.

## Latency:
 Measure the time taken for requests to travel from the client to the service and back. This metric helps assess the overall user experience.


Key metrics for PostgreSQL monitoring:
Read query throughput and performance
Write query throughput and performance
Replication and reliability
Resource utilization: Insufficient CPU or memory can seriously impact application performance. If utilization is high, you may consider increasing the Cloud SQL instance size.Running out of disk space can bring your application to a halt. Even if you’ve opted for automatic storage increases, it’s still a good idea to keep track of disk utilization since these automatic storage increases will add to your GCP costs.
SQL connections: It’s important to ensure that the number of connections to the Cloud SQL MySQL instance doesn’t exceed the connection quota for your GCP project.
Auto-failover requests and replication lag: Auto-failover occurs for HA Cloud SQL database instances when the primary instance becomes unavailable. The amount of time it takes the failover instance to catch up to the primary instance state depends on the replication lag. Ensuring that the replication doesn’t become excessive can speed up failover events and minimize impact to your applications
