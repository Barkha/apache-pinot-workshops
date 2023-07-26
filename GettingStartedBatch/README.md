# Getting Started with Apache Pinot™:  Batch Ingestion

## Introduction

This is an intro level workshop and is designed to get you started with Apache Pinot, familiarize you with its components, and help you run Pinot locally. For this workshop, we will focus on running Pinot locally using a pre-built Docker image and ingesting some batch data.

## Learning Objectives

In this workshop, you will learn:

- The basics of Apache Pinot
- What are the essential components
- How to create tables and schemas
- How to injest batch data
- How to use the Pinot UI

## Prerequisites

In order to run this workshop, you will need the following prerequisites:

1. Docker Desktop
    We will be using Docker to run Pinot locally. If you need to install it, you can go [download Docker Destktop here](https://www.docker.com/get-started/) and follow the intructions to install it.
2. Resources
    Pinot is not designed as a desktop solution. Running it locally needs a minimum of the following resources:
    - 8gb Memory
    - 10 gb disk space

## Challenges

In this workshop, we will be completing three challenges. The challenges build upon each other, so each one needs to be completed for the next one to work.

### 1 - Run Pinot locally on Docker

If you do not have Docker Desktop installed, complete the prerequisite. If you do have Docker Desktop intalled, make sure it's running before moving on to the next steps.

#### 1.1 Pull the docker Image

Use the following command from a command line to pull the Docker image:

```sh
 docker pull apachepinot/pinot:0.12.0
```

On a Windows computer, use a PowerShell (not Windows PowerShell) command window

On a Mac M1, add the -arm64 suffix:

```sh
 docker pull apachepinot/pinot:0.12.0-arm64
```

Verify that this step worked by checking, using the command:

```sh
docker images
```

You should see the Apache Pinot image.

#### 1.2 Run the Docker Container

To run the Docker container, run the following command in the command window:

```sh
docker run -it --entrypoint /bin/bash -p 9000:9000 apachepinot/pinot:0.12.0
```

We are overriding the default entry point of this Docker image with the bash shell. This is to have more control over how the Pinot components are started.

We map the port 9000 of the Docker container to that of the local system, so we can access it via localhost. Port 9000 is used to run the Pinot UI by default.

At this point, you should be running the bash shell in the docker container. Take a moment to look at the contents of the container by listing the contents and looking around.

#### 1.3 Start the Pinot Cluster

In this section, we will start the Pinot cluster.  For our purposes, we will run all four components that are essential to run a Pinot cluster in one docker container. We are only doing this for learning purposes; usually each component would run in its own container.

A typical Pinot cluster consists of the following components:

**Zookeeper** (not strictly a Pinot component, but Pinot depends on it)

To start Zookeeper, run the following command:

```sh
bin/pinot-admin.sh StartZookeeper &
```

Zookeeper is the strongly consistent distributed state store for maintaining the global metadata (e.g. configs and schemas) of the system.

**Pinot Controller**

To start the Pinot controller, run the following command:

```sh
bin/pinot-admin.sh StartController &
```

The Pinot controller is responsible for mapping which servers are responsible for which segments, maintaining admin endpoints, and other management activities for the Pinot cluster.

**Pinot Broker**

To start Pinot broker, run the following command:

```sh
bin/pinot-admin.sh StartBroker &
```

The Pinot Broker is responsible for routing queries to the right servers and consolidating the results.

**Pinot Server**

To start Pinot server, run the following command:

```sh
bin/pinot-admin.sh StartServer &
```

Servers host the data segments and serve queries off the data they host.

To verify that the cluster is running, in a browser, navigate to <http://localhost:9000>

You should see the Pinot UI.  We will discuss the UI further in the upcoming sections.

### 2 - Working with Batch Data

Ingesting data from a filesystem involves the following steps:

- Define a schema
- Define a table config
- Upload the schema and table configs
- Upload the data

For our workshop, we will be using the the configs and data that are part of the docker container we downloaded.

#### 2.1 Exploring the configs

Navigate to the examples/batch folder:

```sh
cd examples/batch
```

You will notice that there are several folders here. Let's navigate to the githubEvents folder:

```sh
cd githubEvents
```

You should see the following files:

- githubEvents_offline_table_config.json
- ingestionJobSpec.yaml
- spartIngestionJobSpec.yaml
- githubEvents_schema.json
- rawdata (folder)

#### 2.2 Create the Offline Table

Use the following command to create the table and schema:

```sh
/opt/pinot/bin/pinot-admin.sh AddTable -schemaFile /opt/pinot/examples/batch/githubEvents/githubEvents_schema.json -tableConfigFile /opt/pinot/examples/batch/githubEvents/githubEvents_offline_table_config.json -exec 
```

At this point, you should be able to verify that the Table and schema were created by navigating to <http://localhost:9000> and selecting tables.

#### 2.3 Ingest Data

Now that we have the table created, let's add some data to the table.
From the folder /opt/pinot, run the following command:

```sh
bin/pinot-admin.sh LaunchDataIngestionJob -jobSpecFile /opt/pinot/examples/batch/githubEvents/ingestionJobSpec.yaml
```

You can verify that the table is populated by navigating to the Pinot UI at <http://localhost:9000> and selecting `Tables` in the left-hand nav. You should see that the table size is greater than 0 MB.

### 3 - Exploring the UI

We have already looked at the UI, but in this section we will explore the Pinot UI.

#### 3.1 Exploring the cluster

Navigate to the URL <http://localhost:9000>. On the home page, you can see the number of controllers, brokers, servers and tables.  When you scroll down, you can see the IP address and ports for each of the Pinot cluster components.

Note that minions are not essential for running the Pinot cluster.  Note also that a tenant is created by default.

#### 3.2 Running Queries

To navigate to the Queries section, select the second option titled 'Query Console' from the left hand side menu. This should show you the tables creates as wellas a query window where you can typ some queries.

You can click on the table name, and it will populate the SQL editor with a defaul query and execute it.

Run the following queries to explore the data:

```sql
select type, count(type) from githubEvents group by type

select actor, count(actor) from githubEvents group by actor order by count(actor) desc

```

Note the timeUseMS and numDocsScanned.

#### 3.3 Exploring the REST APIs

Select the menu item from the left hand side menu titled SWAGGER REST APIs. This should open a new browser tab with SWAGGER end points. Let's check the health of the cluster:

- Select the Cluster 'Get/pinot-controller/admin' option
- select the Try It Out button
- You should see that the cluster is running `GOOD`.

### 4 - Tear down

Since most of the work was done in a Docker container, the tear down is easy. You can either stop the Docker container, or delete it.

- Start a new command window
- Get the name of the container by running 'docker ps'
- Stop the docker container by running 'docker stop'
- Remove (optionally) the container by running 'docker rm'

```sh
docker ps
docker stop <name>
docker rm <name>
```

## References

1. [Startree Developer Website](https://dev.startree.ai)
2. [Apache Pinot Documentation](https://docs.pinot.apache.org/)
3. [Join our slack channel for support](https://stree.ai/slack)

## Contributors

- [Barkha Herman](https://github.com/Barkha)
- [Mark Needham](https://github.com/mneedham)
- [David G Simmons](https://github.com/davidgs)
- [Tim Berglund](https://github.com/tlberglund)
