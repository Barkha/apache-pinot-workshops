# Getting Started with Apache Pinot™: Streaming with Kafka

## Introduction

This is an intro level workshop and is designed to get you started with ingesting streaming data from Kafka with Apache Pinot. In order to complete this workshop, you should have a docker image of pinot already downloaded.

## Learning Obectives

In this workshop, you will:

- Download, install and run Apache Kafka
- Create a online table in Pinot
- Connect Apache Pinot to ingest from Kafka Topic
- Query streaming data as it is ingested

## Prerequisite

In order to run this workshop, you will need the following prerequisites:

- Complete the [previous workshop](../GettingStartedBatch/README.md)
- Resources - since we will run kafka in the existing docker container, make sure you have plenty of space and memory to do so.  We reccomend 8gb memory and 10gb space at minimum.

## Challenges

In this workshop, we will be completing three challenges. The challenges build upon each other, so each one needs to be completed for the next one to work.

### 1 - Download and install Kafka

Let's start with installing kafka.  First, make sure the docker container from the previous session is running.  You can start it like so:

```sh
docker run -it --entrypoint /bin/bash -p 9000:9000 apachepinot/pinot:0.12.0
bin/pinot-admin.sh StartZookeeper &
bin/pinot-admin.sh StartController &
bin/pinot-admin.sh StartBroker &
bin/pinot-admin.sh StartServer &

```

Now, let's run the following command to be able to install kafka.  Docker ps will give you the containerid, which is used to run the docker exec command.

```sh
docker ps
docker exec -it <containerid> bash
```

Next, we will download kafka tar file, untar it, and remove the downloaded file.  Run the following commands, one at a time:

```sh
cd ..
curl https://downloads.apache.org/kafka/3.4.0/kafka_2.12-3.4.0.tgz --output kafka.tgz --output kafka.tgz
tar -xvf kafka.tgz
mv kafka_2.12-3.4.0 kafka
rm -rf kafka.tgz
```

- Note 1: We are downloading the current version.  There maybe newer versions available.
- Note 2: We rename the extracted folder to 'kafka' for simplicity.

Let's start kafka now!

```sh
cd kafka
./bin/kafka-server-start.sh config/server.properties
```

You should now be able to see some new information in zookeeper browser when you navigate to http://localhost:9000.

Note a new set of folders and files such as admin, brokers, cluster etc.

### 2 - Get data from Wikipwdia Events

For the purpose of this workshop, we will use JavaScript to read vents from wikipedia and write to Kafka. 

First, let's create a folder for the real-time data.  From /opt folder, run the following commands:

```sh
cd /opt
mkdir realtime
cd realtime
mkdir events
```

Now, let's download some events in this folder.  In order to do this, we will use a node script to connect to wikipedia and download the events. Let's install node.

```sh
curl -fsSL https://deb.nodesource.com/setup_14.x | bash -
apt install nodejs
```

Wait for installation to complete.  Let's also install vim.  We will use this to edit some files.

```sh
apt install vim
```

In the realtime folder, create the following file:

```sh
vim wikievents.js
```

Cut and paste the contents of the file wikievents.js (in this repo) into int.  Save (:w) & quit (:q).

We will need to install the two modules referenced in the file next:

```sh
npm i eventsource kafkajs
```

you should be able to run it.  Note that this will create a LOT of events in the events folder you created earlier.
*Only run for a few minutes.*

```sh
node wikievents.js
```

You can stop the progema by using Ctrl+C.  You should be able to navigate to the events folder and see a lot of new folders created.  Look at the contents of enwikig.

```sh
cd events
ls
cd enwiki
ls
cd ..
cd ..
```

Next, navigate to http://localhost:9000.  Under the Zookeeper Browser option on the left side, navigate to config->topics.  You should see the wikipedia-events.

We have successfully downloaded some wiki events and added them to Kafka.

### 3 - Configure Pinot for real time ingestion

Now that we have Kafka running and we have some streaming data, let's connect it to Pinot.

For this, we will need to create a new realtime table.  Use the schema and table definitions from this repo to do this.

Create a realtime.schema.json file.

```sh
vim realtime.schema.json
```

Cut and paste the contents of the file from this repo, then save and quit.

Create a realtime.tableconfig.json file.

```sh
vim realtime.tableconfig.json
```

Cut and paste the contents of the file from this repo, then save and quit.

Next, we will create the table using the command below:

```sh
/opt/pinot/bin/pinot-admin.sh AddTable -schemaFile /opt/realtime/realtime.schema.json -tableConfigFile /opt/realtime/realtime.tableconfig.json -exec
```

This should create the table.  You should be able to go to http://localhost:9000 and see the table.  Use the Query Console to view the table and it's contents.

You should be able to look at the content of the table.

```sh
select * from wikievents limit 10
```

Look at the totalDocs.  You could re-run the wikievents.js to consume additional events, and watch the totalDocs updated for each rerun of the query.  You want to stop the wikievents.js or it will fill up your disk :-D.

Notice some of the transformations used in the tableconfig file.  We use the metaJson field to load the nested portion of the wiki event.  We use jsonPath to load data into fields id, stream, domain and topic fields.

### 4 - Teardown

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
