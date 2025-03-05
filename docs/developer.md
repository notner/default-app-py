## Developer Setup

To setup dev environment run: `make dev-setup`.
This will create virtualenv and install requirements.


## Testing (Fixtures)

For testing we need to spin up the services we want to use (kafka, redis, psql, etc), to do this
we have a docker-compose file in `./docker/docker-compose.yaml`.

Start: `make start-fixtures`
Stop: `make stop-fixtures`
Run the tests: `make run-tests`

## Usage

The purpose of this repo is to clone and then build your app's logic ontop.

### Add New Model

To add a new Model, you need to:
```bash
1) define sql table in init.sql  # NB: This makes it available in the psql fixture, expect to write a migration sql for deployment.
2) Create SQLAlchemy model, 'core/model/<name>.py', subclass 'PsqlBase'
3) Access should be defined in 'core/repo/<name>/py'
4) Web Layer in 'web/backend/routes/<name>/py'
```
