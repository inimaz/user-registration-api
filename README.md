# user-registration-api

Goal is to register an user and send them an email with the auth code to validate the registration. See the [architecture overview](./docs/Components%20view.png).

# Install it

```
pip install -r requirements.txt
```

# Run it

```
uvicorn src.main:app --reload
```

# ROADMAP

- [x] Structure of the repo
- [x] [C4 schema](https://c4model.com/) of the solution.
- [ ] Docker deployment
- [ ] docker-compose deployment with DB
- [ ] User registration
- [ ] docker-compose deployment with DB and mocked email server
- [ ] Email sender
