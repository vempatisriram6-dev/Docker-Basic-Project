Dockerized Python + PostgreSQL Mini Project
* This project demonstrates how to use Docker to run a Python application that connects to a PostgreSQL database.
The app:

Connects to PostgreSQL

Creates a table

Inserts one row

Reads and displays the row in a formatted output

This is a perfect beginner-friendly introduction to Docker networking, Python containers, and database connectivity.

# project Structure 

Docker-Practice/
│── app.py
│── Dockerfile
│── requirements.txt
│── README.md

# Step 1: Create Docker Network

   docker network create mynetwork

# Step 2: docker network create mynetwork

docker run -d \
  --name my-postgres \
  --network mynetwork \
  -e POSTGRES_USER=user \
  -e POSTGRES_PASSWORD=pass \
  -e POSTGRES_DB=mydb \
  -p 5432:5432 \
  postgres

# Step 3: Build the Python App Image
  
    docker build -t python_sql .

# Step 4: Run the Python App Container

    docker run --rm --network mynetwork python_sql

# Expected Output :

Connected to the PostgreSQL!

Inserted row ID: 1

All rows in table:

+----+-------------+---------+---------+-----+
| ID | Student No. | Name    | Course  | Age |
+----+-------------+---------+---------+-----+
| 1  | 101         | Sriram  | DevOps  | 22  |
+----+-------------+---------+---------+-----+

# Step 5: Push Image to Docker Hub

    docker login
    docker tag my-python-app vempatisriram2004/python_sql:latest
    docker push vempatisriram2004/python_sql:latest


# Step 6: Pull Image From Docker Hub
      
    docker pull vempatisriram2004/python_sql# Docker-Basic-Project
