# user-registration-api

Goal is to register an user and send them an email with the auth code to validate the registration. See the [architecture overview](./docs/Components%20view.png).

# Structure of the repository

- `docs/` contains the architecture schema.
- `email_server_mock/` contains the mock of the email server.
- `src/` contains the code for the user-api
- `test/` contains all the unit tests.

# ROADMAP

- [x] Structure of the repo
- [x] [C4 schema](https://c4model.com/) of the solution.
- [x] Docker deployment
- [x] docker-compose deployment with DB
- [x] Setup the db
- [ ] User registration logic
  - [x] Create user
  - [x] Send email to user containing the code
- [x] docker-compose deployment with DB and mocked email server
- [ ] Email sender
- [ ] Validate activation code

# Run it

```
docker-compose up -d
```

Go to `localhost:3000/docs` to see the docs of the API

# Run it in local

Same as above but building the source code every time

```
docker-compose up --build
```

# Run the tests

```
# Install general dependencies
pip install -r requirements.txt

# To install pytest + test dependencies
pip install -r requirements.test.txt

# Run the tests
TEST_MODE=true python3 -m pytest
```

Run tests with debug logging

```
TEST_MODE=true python3 -m pytest --log-cli-level=DEBUG -rP
```
