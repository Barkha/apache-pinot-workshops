# Getting Started with Pinot:  Batch Ingestion

## Introduction
This is an intro level workshop and is designed to get you started with Apache Pinot, it's components help you run Pinot locally.  For this workshop, we will focus on running Pinot locally on Docker, and ingesting some batch data.

## Learning Objectives
In this hack, you will:
- Learn the basics of Apache Pinot
- What are the essential components
- How to create tables and schemas
- How to injest batch data
- Get familiar with the Pinot UI

## Prerequisits
In order to run this workshop you will need the following prerequisits:
1. Docker Desktop  
    We will be using Docker to run Pinot locally.  If you need to install it, you can go [here](https://www.docker.com/get-started/) to download and follow the intructions to intall Docker Desktop.
2. Resources
    Pinot is ot designed as a desktop solution.  Running it locally needs a minimum of the following resources:
    - 8gb Memory
    - 10 gb disk space

## Challenges
In this workshop, we will be completing four challenges.  There is also and optional fifth challenge for the more ambitious.  Each challenge needs to be completed for the next one to wrok, since they build upon each other.

### Run Pinot locally on Docker
#### Pull the docker Image
Use the following command from a command line to pull the docker image:

```sh
 docker pull apachepinot/pinot:0.12.0
```
On a Windows computer, use a PowerShell  (not Windows PowerShell) command window

On a Mac M1, add the -arm64 suffix:
```sh
 docker pull apachepinot/pinot:0.12.0-arm64
```
Verify that this step worked by checking, using the command:
```sh
docker images
```
You should see the Apache Pinot image.

#### Run the Docker Container
To run the docker container, run the following command in the command window:
```sh
docker run -it --entrypoint /bin/bash -p 9000:9000 apachepinot/pinot:0.12.0
```
We are overriding the default entry point of this docker image with the bash shell. This is to have more control over how the Pinot components are started.

We map the port 9000 of the Docker container to that of the local system, so we can access it via localhost.  Port 9000 is used to run the Pinot UI by default.

At this point, you should be running the bash shell in the docker container.  Take a moment to look at the contents of the container by listing the contents and looking around.

#### Start Apache Pinot Cluster
In this section, we will start the Pinot cluster.  For our purposes, we will run all four components that are essential to run a Pinot cluster in one docker container.  Typically, this is not the case.

A typical Pinot cluster consists of the following components:

**Zookeeper** (not strictly a Pinot component, but Pinot depends on it)

To start Zookeeper, run the following command:
```sh
bin/pinot-admin.sh StartZookeeper &
```
Zookeeper is used as the persistent metadata store for maintaining global metadata (e.g. configs and schemas) of the system.

**Pinot Controller** 

To start Pinot controller, run the following command:
```sh
bin/pinot-admin.sh StartController &
```
The Pinot controller is responsible for mapping which servers are responsible for which segments, maintaining admin endpoints as well as other management activities for the Pinot cluster.

**Pinot Broker**

To start Pinot broker, run the following command:
```sh
bin/pinot-admin.sh StartBroker &
```
The Pinot broker is responsible for routing queries to the right servers, as well as consolidating the results.

**Pinot Server**

To start Pinot server, run the following command:
```sh
bin/pinot-admin.sh StartServer &
```
Servers host the data segments and serve queries off the data they host. 

To verify that the cluster is running, in a browser, navigate to https://localhost:9000

You should see the Pinot UI.  We will discuss the UI further in the upcoming sections.

### Working with Batch Data
Ingesting data from a filesystem involves the following steps -
- Define Schema
- Define Table Config
- Upload Schema and Table configs
- Upload data
For our workshop, we will be using the the configs and data that is part of the docker container we downloaded.  

Navigate to the /opt/examples/batch folder:
```sh

```
### Exploring the UI
#### Lauch the Apache Pinot UI
### Tear down

## References

## Contributors
- [Barkha Herman](https://github.com/Barkha)
- [Mark Needham](https://github.com/mneedham)
- [David G Simmons](https://github.com/davidgs)