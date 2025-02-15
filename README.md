# Microservice DefaultApp (python)

Versatile start point for building a highly-available, scalable micro-service project.
```code
Tech Stack:
 * Python3 (Flask, SQLAlchemy)
 * Databases:
    - PostreSQL
    - MySQL
 * Events:
    - Kafka
 * Cache:
    - Redis
```
## Design

![](docs/architecture.svg)


## Developer Setup

To setup dev environment run: `make dev-setup`.
This will create virtualenv and install requirements.


## Testing (Fixtures)

For testing we need to spin up the services we want to use (kafka, redis, psql, etc), to do this
we have a docker-compose file in `./docker/docker-compose.yaml`.


Start: `make start-fixtures`

Stop: `make stop-fixtures`

To run the tests:
`make run-tests`
