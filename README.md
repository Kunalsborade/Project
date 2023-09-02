# Install docker desktop 

All the commands are listed here from the beginning.

Pulling images : docker-compose -f docker-compose.yml up

start server : docker-compose up -d

check server : docker-compose ps

close server : docker-compose down

go to the container: docker exec -it kafka /bin/bash

create topic : docker exec -it kafka kafka-topics.sh --create --topic mytopic --partitions 1 --replication-factor 1 --bootstrap-server localhost:9092

list topic : docker exec -it kafka kafka-topics.sh --list --bootstrap-server localhost:9092

delete topic : docker exec -it kafka kafka-topics.sh --delete --topic mytopic --bootstrap-server localhost:9092

create producer : docker exec -it kafka kafka-console-producer.sh --topic mytopic --bootstrap-server localhost:9092

create consumer : docker exec -it kafka kafka-console-consumer.sh --topic mytopic --bootstrap-server localhost:9092 --from-beginning


database setup : 
1. Open PGAdmin: Go to http://localhost:5050 in your web browser, and you should see the PGAdmin login page
    Log in using the email and password you specified in your docker-compose.yml file.
2. Add a Server:
    Click on the "Servers" menu on the left-hand side.
    Right-click on "Servers" and choose "Create" and then "Server..." to open the "Create - Server" dialog.
3. General Tab:
    In the "Name" field, enter a name for your server.
4. Connection Tab:
    In the "Host name/address" field, enter the name of your PostgreSQL container, which is usually the name you specified in the docker-compose.yml file.
    In the "Port" field, enter "5432," which is the default PostgreSQL port.
    In the "Maintenance database" field, enter the name of your database.
    In the "Username" field, enter the PostgreSQL username.
    In the "Password" field, enter the PostgreSQL password.
5. Save the Server:
    Click the "Save" button.
6. Connect to the Server:
    In the left sidebar, under "Servers," you should now see the server you just created. Click on it to connect.
