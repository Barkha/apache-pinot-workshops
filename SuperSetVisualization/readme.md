# Getting Started with Apache Pinot™: Visualization with SuperSet

## Introduction

Apache Superset is an open-source data visualization and data exploration platform designed to be highly intuitive and visually appealing. It allows users to create and share interactive dashboards and visualizations, supporting a wide array of data sources. Superset's strength lies in its ability to provide a user-friendly interface for exploring and visualizing large datasets, making data analysis accessible to non-technical users.

Apache Pinot, on the other hand, is a real-time distributed OLAP datastore, optimized for low-latency, high-throughput analytical queries. It is designed to provide instant insights on data at scale, making it a popular choice for applications in time-sensitive data analysis scenarios.

Pairing Apache Superset with Apache Pinot makes sense due to the complementary strengths of the two systems. While Pinot provides the backend infrastructure capable of querying massive datasets at high speed, Superset offers the front-end interface that allows users to explore, visualize, and share those insights easily. Together, they form a powerful stack for real-time analytics, enabling users to derive actionable insights from their data rapidly.

## Learning Objective

By the end of this article, you will learn:

1. The basic concepts and features of Apache Superset and Apache Pinot.
2. How to integrate Apache Superset with Apache Pinot to leverage real-time data analytics.
3. The steps to configure a data source in Superset connected to a Pinot cluster.
4. How to use Apache Superset's UI to create dynamic and interactive dashboards based on data from Apache Pinot.

## Prerequisite

Before diving into the process, you should have the following:

* A basic understanding of data visualization concepts.
* Docker installed and running in your environment.

## Step By Step instructions

### Deploying Superset and Pinot

In order to support SuperSet with Pinot, I am using docker compose.

```sh
docker run \
  --network pinot-demo \
  --name=superset \
  -e "SUPERSET_SECRET_KEY=<YOUR_SECRET_KEY>" \
  -p 8088:8088 \
  -d apachepinot/pinot-superset:latest

```

NOTE: You will need to create a 

### Setup Admin account

This step sets up Superset Admin account.  It needs to be run once per container.

```sh
docker exec -it superset superset fab create-admin \
              --username admin \
              --firstname Admin \
              --lastname Admin \
              --email admin@localhost \
              --password admin
```

### DB upgrade and initialize Superset

```sh
docker exec -it superset superset db upgrade
docker exec -it superset superset init
```

### Import Pre-Built Pinot Datasource and Dashboard

```sh
docker exec \
    -t superset \
    bash -c 'superset import_datasources -p /etc/examples/pinot/pinot_example_datasource_quickstart.yaml && \
             superset import_dashboards -p /etc/examples/pinot/pinot_example_dashboard.json'
```