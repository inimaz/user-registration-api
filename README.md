# user-registration-api

Goal is to register an user and send them an email with the auth code to validate the registration. See the [architecture overview](./docs/Components%20view.png).

# ROADMAP

- [x] Structure of the repo
- [x] [C4 schema](https://c4model.com/) of the solution.
- [x] Docker deployment
- [x] docker-compose deployment with DB
- [ ] User registration logic
- [ ] docker-compose deployment with DB and mocked email server
- [ ] Email sender

# Run it

```
docker-compose up -d
```

Go to `localhost:3000/docs` to see the docs of the API

# Run it in local

Same as above but with hot reloading of the src folder

```
docker-compose -f docker-compose.dev.yml up -d
```

# Run the tests

```
pip install -r requirements.txt
// TODO:
```
