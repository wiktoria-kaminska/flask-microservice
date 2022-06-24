# Participant Registry Microservice


A  sample Python application that demonstrates simple usage of the REST API and CRUD operations.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies defined in the [requirements file](requirements.txt), optionally using a virtual environment.

```bash
# create virtual python environment for the project
python3 -m venv venv

# install dependencies
python3 -m pip install -r requirements.txt
```

## Usage

### Starting the development server
To start the server in development mode on `127.0.0.1:5000`:
```
flask run
```
### Running tests
```
pytest
```
## Endpoints

- `GET api/participants` Retrieve all participants 
- `GET api/participants/<participant_ref>` : Retrieve single participant data
- PUT/POST api/participants/<participant_ref> : Create/Update single participant data 
- DELETE api/participants/<participant_ref> : Delete participant

## License
[MIT](https://choosealicense.com/licenses/mit/)
