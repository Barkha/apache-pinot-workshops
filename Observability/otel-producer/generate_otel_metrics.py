import json
import time
import random
from confluent_kafka import Producer, KafkaError

def delivery_report(err, msg):
    """
    Callback for Kafka message delivery.
    
    Args:
        err: Error information (if any).
        msg: Delivered message metadata.
    """
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [partition {msg.partition()}] at offset {msg.offset()}")

def create_kafka_producer(bootstrap_servers='localhost:9092'):
    """
    Create and return a Kafka Producer instance.
    
    Args:
        bootstrap_servers (str): Kafka bootstrap servers.
    
    Returns:
        Producer: Configured Kafka Producer.
    """
    conf = {
        'bootstrap.servers': bootstrap_servers,
        'client.id': 'otel-metrics-producer'
    }
    return Producer(conf)

def generate_and_send_otel_metrics(num_metrics, kafka_producer, kafka_topic='otel-metrics'):
    """
    Generate OTEL Metrics and send each to a Kafka topic.
    
    Args:
        num_metrics (int): Number of metrics to generate.
        kafka_producer (Producer): Confluent Kafka Producer instance.
        kafka_topic (str): Kafka topic to send messages to.
    """
    # Base timestamp (current time in nanoseconds)
    base_time_ns = int(time.time() * 1_000_000_000)
    
    # Possible values for randomization
    service_names = ["auth-service", "order-service", "payment-service", "inventory-service"]
    environments = ["production", "staging", "development"]
    regions = ["us-east", "us-west", "eu-central", "ap-south"]
    transaction_types = ["credit", "debit", "refund"]
    endpoints = ["/api/login", "/api/order", "/api/payment", "/api/inventory"]
    error_codes = ["timeout", "not_found", "server_error"]
    protocols = ["http", "grpc", "websocket"]
    
    # Base OTEL structure template
    otel_template = {
        "resourceMetrics": [
            {
                "resource": {
                    "attributes": [
                        {"key": "service.name", "value": {"stringValue": random.choice(service_names)}},
                        {"key": "environment", "value": {"stringValue": random.choice(environments)}}
                    ]
                },
                "scopeMetrics": [
                    {
                        "scope": {
                            "name": "transaction.library",
                            "version": f"{random.randint(1, 3)}.{random.randint(0, 5)}.{random.randint(0, 9)}",
                            "attributes": [
                                {"key": "region", "value": {"stringValue": random.choice(regions)}}
                            ]
                        },
                        "metrics": []
                    }
                ]
            }
        ]
    }
    
    # Metric types and configurations
    metric_types = [
        {
            "type": "sum",
            "name": "transaction.count",
            "unit": "1",
            "description": "Counts the number of transactions processed",
            "is_monotonic": True,
            "attr_key": "transaction.type",
            "attr_values": transaction_types
        },
        {
            "type": "gauge",
            "name": "transaction.latency",
            "unit": "ms",
            "description": "Measures transaction processing latency",
            "attr_key": "endpoint",
            "attr_values": endpoints
        },
        {
            "type": "histogram",
            "name": "error.rate",
            "unit": "1",
            "description": "Histogram of error occurrences",
            "attr_key": "error.code",
            "attr_values": error_codes
        },
        {
            "type": "exponentialHistogram",
            "name": "request.size",
            "unit": "bytes",
            "description": "Exponential histogram of request sizes",
            "attr_key": "protocol",
            "attr_values": protocols
        }
    ]
    
    # Generate and send the specified number of metrics
    for i in range(num_metrics):
        # Create a fresh OTEL structure for each metric
        otel_data = json.loads(json.dumps(otel_template))  # Deep copy
        otel_data["resourceMetrics"][0]["resource"]["attributes"][0]["value"]["stringValue"] = random.choice(service_names)
        otel_data["resourceMetrics"][0]["resource"]["attributes"][1]["value"]["stringValue"] = random.choice(environments)
        otel_data["resourceMetrics"][0]["scopeMetrics"][0]["scope"]["version"] = f"{random.randint(1, 3)}.{random.randint(0, 5)}.{random.randint(0, 9)}"
        otel_data["resourceMetrics"][0]["scopeMetrics"][0]["scope"]["attributes"][0]["value"]["stringValue"] = random.choice(regions)
        
        # Randomly select a metric type
        metric_config = random.choice(metric_types)
        metric_type = metric_config["type"]
        
        # Common fields for the metric
        metric = {
            "name": f"{metric_config['name']}_{i % 4}",  # Unique name for variety
            "unit": metric_config["unit"],
            "description": metric_config["description"]
        }
        
        # Generate data point
        data_point = {
            "timeUnixNano": str(base_time_ns + random.randint(0, 1_000_000_000)),
            "attributes": [
                {
                    "key": metric_config["attr_key"],
                    "value": {"stringValue": random.choice(metric_config["attr_values"])}
                }
            ]
        }
        
        if metric_type == "sum":
            data_point["asDouble"] = random.uniform(10, 100)
            data_point["startTimeUnixNano"] = str(base_time_ns)
            metric["sum"] = {
                "aggregationTemporality": 1,
                "isMonotonic": metric_config.get("is_monotonic", False),
                "dataPoints": [data_point]
            }
        
        elif metric_type == "gauge":
            data_point["asDouble"] = random.uniform(50, 500)
            metric["gauge"] = {
                "dataPoints": [data_point]
            }
        
        elif metric_type == "histogram":
            data_point["startTimeUnixNano"] = str(base_time_ns)
            data_point["count"] = random.randint(1, 10)
            data_point["sum"] = random.uniform(1, 10)
            data_point["bucketCounts"] = [random.randint(0, 5), random.randint(0, 5)]
            data_point["explicitBounds"] = [random.uniform(1, 5)]
            data_point["min"] = random.uniform(0, 1)
            data_point["max"] = random.uniform(2, 10)
            metric["histogram"] = {
                "aggregationTemporality": 1,
                "dataPoints": [data_point]
            }
        
        elif metric_type == "exponentialHistogram":
            data_point["startTimeUnixNano"] = str(base_time_ns)
            data_point["count"] = random.randint(1, 20)
            data_point["sum"] = random.uniform(100, 5000)
            data_point["scale"] = random.randint(0, 2)
            data_point["zeroCount"] = random.randint(0, 5)
            data_point["positive"] = {
                "offset": random.randint(0, 2),
                "bucketCounts": [random.randint(0, 10), random.randint(0, 10)]
            }
            data_point["min"] = random.uniform(0, 1000)
            data_point["max"] = random.uniform(1000, 10000)
            data_point["zeroThreshold"] = 0
            metric["exponentialHistogram"] = {
                "aggregationTemporality": 1,
                "dataPoints": [data_point]
            }
        
        # Add the metric to the OTEL structure
        otel_data["resourceMetrics"][0]["scopeMetrics"][0]["metrics"] = [metric]
        
        # Serialize and send to Kafka
        try:
            message = json.dumps(otel_data)
            kafka_producer.produce(
                topic=kafka_topic,
                value=message.encode('utf-8'),
                callback=delivery_report
            )
            # Poll to handle delivery callbacks
            kafka_producer.poll(0)
        except KafkaError as e:
            print(f"Failed to send metric {i+1} to Kafka: {e}")
    
    # Flush the producer to ensure all messages are sent
    kafka_producer.flush()
    print(f"Sent {num_metrics} metrics to Kafka topic '{kafka_topic}'")

# Example usage
if __name__ == "__main__":
    # Kafka configuration
    bootstrap_servers = 'kafka:9092'  # Update as needed
    kafka_topic = 'otel_metrics'
    
    # Number of metrics to generate
    num_metrics_to_generate = 5
    
    # Create Kafka producer
    producer = create_kafka_producer(bootstrap_servers)
    
    # Generate and send metrics
    generate_and_send_otel_metrics(num_metrics_to_generate, producer, kafka_topic)