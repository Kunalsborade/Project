# Backend README

## Installing Docker Desktop

1. Install Docker Desktop by following the official installation instructions for your operating system.

## Setting up the Virtual Environment

1. Create a virtual environment:
"python -m venv venv_name"

2. Activate the virtual environment:
"venv_name\Scripts\activate" # Windows
"source venv_name/bin/activate" # Linux/macOS

## Installing Backend Requirements

1. Install Backend requirements from the `requirements.txt` file:
"pip install -r requirements.txt"

## Working with Docker

### Pulling Docker Images

1. Pull images specified in the `docker-compose.yml` file:

"docker-compose -f docker-compose.yml up"

### Starting the Server

1. Start the server in detached mode (runs in the background):

"docker-compose up -d"

### Checking Server Status

1. Check the status of the running containers:

"docker-compose ps"

### Stopping the Server

1. Stop and remove the running containers:

"docker-compose down"

### Accessing a Container

1. Access a running container interactively (example with a container named "kafka"):

"docker exec -it kafka /bin/bash"

### Managing Kafka Topics

1. Create a Kafka topic:

"docker exec -it kafka kafka-topics.sh --create  --partitions 1 --replication-factor 1 --bootstrap-server localhost:9092 --topic mytopic"

2. List Kafka topics:

"docker exec -it kafka kafka-topics.sh --bootstrap-server localhost:9092 --list"


3. Delete a Kafka topic:

docker exec -it kafka kafka-topics.sh --bootstrap-server localhost:9092 --delete --topic mytopic

### Working with Kafka Producers and Consumers

1. Create a Kafka producer:

"docker exec -it kafka kafka-console-producer.sh --topic mytopic --bootstrap-server localhost:9092"

2. Create a Kafka consumer:

"docker exec -it kafka kafka-console-consumer.sh --topic mytopic --bootstrap-server localhost:9092 --from-beginning"

## Database Setup

1. Open PGAdmin by visiting http://localhost:5050 in your web browser and log in using the credentials specified in your `docker-compose.yml` file.

2. Add a Server:
- Click on the "Servers" menu on the left-hand side.
- Right-click on "Servers" and choose "Create" and then "Server..." to open the "Create - Server" dialog.

3. General Tab:
- Enter a name for your server in the "Name" field.

4. Connection Tab:
- Enter the name of your PostgreSQL container in the "Host name/address" field (usually the name you specified in the `docker-compose.yml` file).
- Enter "5432" in the "Port" field (the default PostgreSQL port).
- Specify the "Maintenance database," "Username," and "Password" as per your configuration.

5. Save the Server: Click the "Save" button.

6. Connect to the Server: You should now see the server you created under "Servers" in the left sidebar. Click on it to connect.

