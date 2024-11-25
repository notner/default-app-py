# Default App (Python)

Basic webapp structure using Python.

Tech:
 * Python
 * Flask
 * SQLAlchemy
 * PostreSQL
 * Kafka
 * Redis

## Developer Setup

To setup dev environment run: `make dev-setup`
This will create virtualenv and install requirements


## Testing (Fixtures)

For testing we need to spin up the services we want to use (kafka, redis, psql, etc), to do this
we have a docker-compose file in `./docker/docker-compose.yaml`.

Start: `make start-fixtures`
Stop: `make stop-fixtures`

To run the tests:
`make run-tests`
