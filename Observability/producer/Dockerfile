FROM python:3.12.3-slim

RUN apt-get update -y && \
    apt-get install -y librdkafka-dev

WORKDIR /code
COPY requirements.txt requirements.txt
COPY generate_otel_metrics.py generate_otel_metrics.py

RUN pip install --upgrade pip
RUN python3 --version && pip install -r requirements.txt

CMD ["python", "generate_otel_metrics.py"]