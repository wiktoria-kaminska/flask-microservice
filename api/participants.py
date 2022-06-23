from flask import Blueprint
from flask import jsonify
from flask import request
from .models import Participant
from .reference_utils import validate_ref

# mock database
participant_dict = {}

def reset_database():
    global participant_dict
    participant_dict = {}

participants = Blueprint('participants', __name__)

@participants.route('/participants', methods=['GET'])
def find_all_participants():
    '''Returns all participants'''
    return jsonify(list(participant_dict.values()))


@participants.route('participants/<participant_ref>', methods=['GET'])
def find_single_participant(participant_ref):
    '''Returns specific participant based on provided participant ID'''
    if validate_ref(participant_ref) is False:
        return f'Bad reference {participant_ref}', 400

    if participant_ref in participant_dict:

        return jsonify(participant_dict[participant_ref])

    return 'Not found', 404


@participants.route('/participants/<participant_ref>', methods=['POST', 'PUT'])
def create_participant(participant_ref):
    '''Stores data under provided ID'''

    if not validate_ref(participant_ref):
        return f'bad reference {participant_ref}', 400

    try:
        participant = Participant.from_dict(request.json)
        exists = participant_ref in participant_dict
        participant_dict[participant_ref] = participant
        code = 200 if exists else 201
        print(f'adding participant with ref: {participant_ref}, exists: {exists}, code: {code}')
        return "success", code
    except KeyError as error:
        print(f'Unable to deserialise from data: {request.json} with error: {error}')
        return 'Deserialisation error', 400
    except ValueError as error:
        print(f'Error in the {error} field')
        return f'Invalid {error}', 400

    except error:
        return 'Uknown error', 400


@participants.route('/participants/<participant_ref>', methods=['DELETE'])
def delete_participant(participant_ref):
    '''Deletes data stored under provided ID'''
    if validate_ref(participant_ref) is False:
        return f'Bad reference {participant_ref}', 400

    if participant_ref in participant_dict:

        del participant_dict[participant_ref]
        return 'Deleted', 200

    return 'Not found', 404
