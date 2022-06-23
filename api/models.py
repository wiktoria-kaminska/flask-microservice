from dataclasses import dataclass
from dataclasses_json import dataclass_json
import re
import time

def validate_fields(participant):
    valid_name = re.fullmatch(r"^[\-'a-zA-Z ]+$", participant.name)
    valid_dob = time.strptime(participant.dob, '%d/%m/%Y')
    valid_phone = re.fullmatch(r'^(07[\d]{8,12}|447[\d]{7,11})$',participant.phone)
    
    if valid_name is None: 
        print('Invalid name')
        message = ('name')
        return ValueError(message)

    if valid_name is None:
        print('Invalid date of birth')
        message = ('date of birth')
        return ValueError(message)

    if valid_phone is None:
        print('Invalid phone number')
        message = ('phone')
        return ValueError(message)
    

    print('Valid Number')


@dataclass_json
@dataclass
class Participant:
    '''Represents or models a single participant'''
    name: str
    dob: str
    phone: int
    address: str

    def __post_init__(self):
        error =  validate_fields(self)
        if error:
            raise error