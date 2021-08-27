# schlepwise-api
backend API to track domestic labor

## Running locally

To build and run a local instance, use docker; First build the image with the API server:

```bash
docker build -t schlepwise-api_schlepwise_local:latest .
```

Then spin up containers with a local Postges database and Flask API, which you can visit at `localhost:4000/`

```bash
docker-compose up -d schlepwise_local
```



To spin down the containers:

```bash
docker-compose down
```
