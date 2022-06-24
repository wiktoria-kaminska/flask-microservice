# Participant Registry Microservice


A sample Python application that demonstrates simple usage of a REST API and CRUD operations.

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

To test endpoints and reference utils:

```
pytest
```
## Endpoints

- `GET api/participants` Retrieve all participants 
- `GET api/participants/<participant_ref>` : Retrieve single participant data
- `PUT/POST api/participants/<participant_ref>` : Create/Update single participant data 
- `DELETE api/participants/<participant_ref>` : Delete participant


## Notes

With the given problem in mind, the structure of this application implements the CRUD architecture.

In addition to the main application, the project also contains some utility functions to simulate the second microservice which assigns random reference numbers to participants. 
Its worth pointing out that the generated references have a different format to the example specified in the task, the idea was to create any kind of random string to demonstrate how it can be used and validated. As all CRUD operations in this application (except GET all participants) rely on unique reference number, it was important to demonstrate at least some very basic validation. With a confirmed unique reference format it would be beneficial to add more validation criteria to reduce potential errors. 

Participant data is stored in a `dataclass`. The main purpose of using dataclasses was to reduce boilerplate code and improve readability.
In comparison to dictionaries (which was the initial plan for storing data), dataclasses almost always have a smaller memory foot-print, but are also much slower. Further testing would be needed to see if using dataclass instead of dictionary (or other data types) in this particular scenario has any meaningful impact.  In a more complex scenario and depending on the user's needs, it could be worth to rethink the current data storage. 

The data fields for `Participant` are all primitives, text data is represented with strings and the phone number is an integer. Looking back, representing date of birth with a string instead of date from `datetime` library may not have been the best idea. Using date would make it easier for the app to be extended to allow data retrieval based on attributes like age which would be useful in the context of this task (to answer questions like "how many participants are in this age range?"). 

Similarly, using a string to store the address also has its limitations. It works, but it makes validation and searching for specific fields within the address quite difficult. There is nothing stopping the user from just entering the house number without a street name, or providing a postcode which is invalid for the specified country. Adding an address class and storing the address using it would provide more flexibility as it would allow to search specific groups of participants  (e.g participants who live in a certain country) and perform more thorough validation.
