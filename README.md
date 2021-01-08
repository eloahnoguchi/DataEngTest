# DataEngTest
Data Engineering Test

## Requirements

- Docker version >= 19.03
- Docker-compose version >= 1.25

Instruction on how to install [docker](https://docs.docker.com/get-docker/) and [docker-compose](https://docs.docker.com/compose/install/).


## Firing up your Data Base

Fire up your PostgreSQL instance by opening a terminal and running the following command:

```bash
docker-compose up -d 
```

Using your prefered DB Client ([DBeaver](https://dbeaver.io/) for instace), you can connect to your PostgreSQL instance with the following credentials:

```
HOST: localhost
PASSWORD: 5342
USER: kzas
PASSWORD: kzas
DB: kzas
```

---
### The task ahead

The following diagram describe what you should do:


You have a folder (`raw_data`) that contains JSON data from real estate ads and a CSV file with information about buildings. 
It's required that you write a script to identify for each ad, which building it belongs to. After successfully identifying that an ad X belongs to building Y, load the enriched ad data into a PostgreSQL table (or set of tables). 
You should also provide the sql statements to create the table(s) into PostgreSQL database.
