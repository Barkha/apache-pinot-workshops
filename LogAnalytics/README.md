# Sample app uses Apache Pinot for Log Anlaytics

## Introduction

## Objective

## Installation

Run the environment

```sh
docker-compose up -d
```

Run the following command for creating topic in the Kafka Container:

```sh
 docker exec workshop-kafka ./opt/bitnami/kafka//bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic logs
 ```

 Run command to create tables in the Pinot Controller container

```sh
./bin/pinot-admin.sh AddTable -schemaFile /scripts/schema.json -tableConfigFile /scripts/table.json -controllerHost pinot-controller -exec
```

 Run command to update Superset:

 This step sets up Superset Admin account.  It needs to be run once per container.

```sh
docker ps # to get the container id
docker exec -it <containerid> superset fab create-admin --username admin --firstname Superset --lastname Admin --email admin@superset.com --password admin
docker exec -it <containerid> superset db upgrade
docker exec -it <containerid> superset init
```

## Details

### Architecture

In this demo app, we simulate an observability usecase.  We use a simple log generator that emulated HTTPS response logs, using a python script. This log is then posted to a Kafka Topic. Next, Apache Pinot ingests the said message, and allows for realtime querying the data. We use Superset to create the dashboards that diaplay realtime counts of errors, ewrror types etc.

![Log Analytics Architecture](/images/LogAnalyticsArchitecture.png) "Log Analytics Architecture"

#### Samples log

Here's an example of the simplified log format we will be using:

``` json
{
    'ip': '192.168.198.92',
    'timestamp': '2024-09-08 10:45:23',
    'method': 'GET',
    'uri':'/',
    'protocol':'HTTPS',
    'version':'1.2'.
    'response-code': 200,
    'time': 6394,
    'domain': 'www.test.com'
}
```

Here's a list of methods we will be using:

- CONNECT
- DELETE
- GET
- HEAD
- OPTIONS
- PATCH
- POST
- PUT
- TRACE

Here's a list of Reposnses we will be using:

- 100
- 200
- 300
- 400
- 500

Note that we are keeping it brief for demo pusposes.  I know that there are more response codes for an HTTp request.

The python script creates a message per second, and ends it to the Kafka topic logs. 

## Teardown

To tear down run the following docker command:

``` docker
docker-compose down
```