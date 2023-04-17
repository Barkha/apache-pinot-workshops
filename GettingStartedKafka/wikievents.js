var EventSource = require("eventsource");
var fs = require("fs");
var path = require("path");
const { Kafka } = require("kafkajs");

var url = "https://stream.wikimedia.org/v2/stream/recentchange";

const kafka = new Kafka({
  clientId: "wikievents",
  brokers: ["localhost:9092"],
});

const producer = kafka.producer();

async function start() {
  await producer.connect();
  startEvents();
}

function startEvents() {
  console.log(`Connecting to EventStreams at ${url}`);
  var eventSource = new EventSource(url);

  eventSource.onopen = function () {
    console.log("--- Opened connection.");
  };

  eventSource.onerror = function (event) {
    console.error("--- Encountered error", event);
  };

  eventSource.onmessage = async function (event) {
    const data = JSON.parse(event.data);
    const eventPath = path.join(__dirname, "./events", data.wiki);
    fs.existsSync(eventPath) || fs.mkdirSync(eventPath);
    fs.writeFileSync(path.join(eventPath, data.meta.id + ".json"), event.data);
    await producer.send({
      topic: "wikipedia-events",
      messages: [
        {
          key: data.meta.id,
          value: event.data,
        },
      ],
    });
  };
}

start();