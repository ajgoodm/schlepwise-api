#!/bin/bash

set -e

docker compose down
docker build -t schlepwise-api_schlepwise_local:latest .
docker-compose up -d schlepwise_local 