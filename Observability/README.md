# Observability With OTEL, Kafka, Pinot and Superset

## Introduction

OpenTelemetry (OTEL) is a collection of APIs, SDKs, and tools that provide high-quality, ubiquitous, and portable telemetry to enable effective observability.

Apache Kafka is an open-source distributed event streaming platform used by thousands of companies for high-performance data pipelines, streaming analytics, data integration, and mission-critical applications.

Apache Superset is an open-source data visualization and data exploration platform designed to be highly intuitive and visually appealing.

Apache Pinot is a real-time distributed OLAP datastore, optimized for low-latency, high-throughput analytical queries. It is designed to provide instant insights on data at scale, making it a popular choice for applications in time-sensitive data analysis scenarios.

Pairing these technologies provides an Open Source, disaggregated, scalable and real-time Observability platform that solves for data freshness, scale as well a defragmentation of system information.

## Learning Objective

By the end of this workshop, you will learn:

1. The basic concepts and features of OTEL, Apache Kafka, Apache Superset and Apache Pinot.
2. How to integrate Apache Superset with Apache Pinot to leverage real-time data analytics.
3. The steps to configure a data source in Superset connected to a Pinot cluster.
4. How to use Apache Superset's UI to create dynamic and interactive dashboards based on data from Apache Pinot.

## Prerequisite

Before diving into the process, you should have the following:

* A basic understanding of data visualization concepts.
* Docker installed and running in your environment.

## Step By Step instructions

### Deploying Superset and Pinot

In order to support SuperSet with Pinot, I am using docker compose.  Run the following command to run Superset and Pinot instaces.

```sh
docker-compose up -d 
```

You can verify deployment - which takes a few minutes to start by launching the following URLs:

* <http://localhost:9000> <- Pinot deployment
* <https://localhost:8088> <- Superset deployment

### Setup Admin account

This step sets up Superset Admin account.  It needs to be run once per container.

```sh
docker ps # to get the container id
docker exec -it <containerid> superset fab create-admin --username admin --firstname Superset --lastname Admin --email admin@superset.com --password admin
docker exec -it <containerid> superset db upgrade
docker exec -it <containerid> superset init
```

### Import Pre-Built Pinot Datasource and Dashboard

Superset supports import/export for Dashboards, charts, datasets and database connections.  In this excercise, we will import a dashboard with four charts.  The charts display data from the AirlineStats table in the PInot Quickstart.

* To import, navigate to the dashboard, and select the import icon as shown below:
![SuperSet Import](/images/superset-import.png "SuperSet Import")
* Click on Import File.
* Import the file "dashboar_export_airlinestat.zip"
![SuperSet Import](/images/superset-import-2.png "SuperSet Import: Select File")
* This should import the data connection, datasets, charts and dashboard.
![SuperSet Import](/images/superset-dashboard.png "SuperSet Import: Select File")

Feel free to explore the interface, charts etc.

### Teardown

To stop the running containers, use the following command:

```sh
docker-compose down
```

### Conclusion

There you have it!  We have successfully deployed Superset and Pinot, working together, and run some dashboards on Superset.