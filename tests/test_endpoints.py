
from tests.base_test_case import BaseTestCase
from api.models import Participant


VALID_PARTICIPANT = Participant(
    name="Wiktoria Kaminska",
    dob="09/09/1998",
    phone="07871567890",
    address="1 Random Way, Ipswich, IP11IP"
)

MODIFIED_PARTICIPANT = Participant(
    name="Kaminska Wiktoria",
    dob="09/09/1999",
    phone="07771567777", 
    address="1 Random Way, Ipswich, IP11IP"
)

INVALID_PARTICIPANT_JSON = '{"name": "Wiktoria", "dob":"01/01/1998", "phone":"gdfhh", "address":"1 Random Way, Ipswich, IP11IP"}'

VALID_REFERENCE = 'ABCDE12345'
INVALID_REFERENCE = '%$1919123'

def is_success(status_code: int):
    return status_code >= 200 and status_code < 300


class ParticipantEndpointTests(BaseTestCase):
    def test_fresh_instance_get_returns_empty(self):
        '''Ensure the API returns empty participant list initially'''
        response = self.client.get('api/participants')
        assert response.json == []
        assert response.status_code == 200

    def test_get_idempotent(self):
        '''Test GET twice in a row without POST or PUT inbetween returns same result'''
        # test idempotency with empty results
        response1 = self.client.get('api/participants')
        response2 = self.client.get('api/participants')
        assert response1.json == response2.json

        # create a record
        response = self.client.post(
            f'api/participants/{VALID_REFERENCE}',
            data=VALID_PARTICIPANT.to_json(),
            content_type='application/json',
        )
        assert is_success(response.status_code)

        # test idempotency with non-empty results
        response1 = self.client.get('api/participants')
        response2 = self.client.get('api/participants')
        assert response1.json == response2.json


    def test_get_nonexistant(self):
        '''test GET on resource that doesn't exist returns 404'''
        response = self.client.get(f'api/participants/{VALID_REFERENCE}')
        print(response.json)
        assert response.status_code == 404


    def test_put_bad_data(self):
        '''Ensure bad request error is returned for garbage request bodies'''
        response = self.client.post(
            f'api/participants/{VALID_REFERENCE}',
            data=INVALID_PARTICIPANT_JSON,
            content_type='application/json',
        )
        assert response.status_code == 400


    def test_successful_post(self):
        '''Ensure a put request with a valid body and resource id successfully adds a participant'''
        put_response = self.client.put(
            f'api/participants/{VALID_REFERENCE}',
            data=VALID_PARTICIPANT.to_json(),
            content_type='application/json',
        )
        assert put_response.status_code == 201

        get_response = self.client.get(f'api/participants/{VALID_REFERENCE}')
        assert get_response.status_code == 200

        # Ensure the created participant matches the request data
        returned_participant = Participant.from_dict(get_response.json)
        assert returned_participant == VALID_PARTICIPANT

        
    def test_successful_post(self):
        '''Ensure a put request with a valid body and resource id successfully adds a participant'''
        post_response = self.client.post(
            f'api/participants/{VALID_REFERENCE}',
            data=VALID_PARTICIPANT.to_json(),
            content_type='application/json',
        )
        assert post_response.status_code == 201

        get_response = self.client.get(f'api/participants/{VALID_REFERENCE}')
        assert get_response.status_code == 200

        # Ensure the created participant matches the request data
        returned_participant = Participant.from_dict(get_response.json)
        assert returned_participant == VALID_PARTICIPANT


    def test_successful_put_update(self):
        '''Ensure a put request with a valid body and resource id successfully adds a participant'''
        put_response = self.client.put(
            f'api/participants/{VALID_REFERENCE}',
            data=VALID_PARTICIPANT.to_json(),
            content_type='application/json',
        )
        # When the resource is created for the first time, status code 201 should be returned
        assert put_response.status_code == 201

        update_response = self.client.put(
            f'api/participants/{VALID_REFERENCE}',
            data=MODIFIED_PARTICIPANT.to_json(),
            content_type='application/json',
        )

        # When updating an existing resource, status code 200 should be returned
        assert update_response.status_code == 200

        # Ensure the resource has been successfully updated
        get_response = self.client.get(f'api/participants/{VALID_REFERENCE}')
        assert get_response.status_code == 200
        returned_participant = Participant.from_dict(get_response.json)
        assert returned_participant == MODIFIED_PARTICIPANT


    def test_add_with_bad_reference(self):
        '''Ensure bad request error is returned when attempting to insert with an invalid reference'''
        response = self.client.post(
            f'api/participants/{INVALID_REFERENCE}',
            data=VALID_PARTICIPANT.to_json(),
            content_type='application/json',
        )

        assert response.status_code == 400
