import json
from datetime import datetime, timedelta

from footium_api import GqlConnection
from footium_api.queries import get_server_timestamp


def prepare_lineup_to_sign(gql: GqlConnection, lineup):
    current_time = get_server_timestamp(gql)
    current_time_local = datetime.utcnow()
    current_time = current_time / 1000.0
    current_time = datetime.utcfromtimestamp(current_time)
    timeout = 1000*5*60
    expiration_time = current_time + timedelta(milliseconds=timeout)
    # expiration_iso_string = expiration_time.isoformat() + 'Z'
    expiration_iso_string = expiration_time.isoformat(timespec='milliseconds') + 'Z'

    message = {
        # "id": -1,
        "type": "LINEUP_SET",
        "data": {
            "lineup": {
                "id": lineup.id,
                "clubId": lineup.clubId,
                "isSelected": lineup.isSelected,
                "tacticsId": lineup.tacticsId,
            },
            "tactics": {
                "id": lineup.tactics.id,
                "mentality": lineup.tactics.mentality,
                "formationId": lineup.tactics.formationId,
            },
            "playerLineups": lineup.playerLineups.to_list(),
        },
        # "timestamp": timestamp,
        "expirationTime": expiration_iso_string,
    }
    return json.dumps(message)
    # return message

def submit_lineup(gql: GqlConnection, message, signed_message, address):
    query = """
mutation SubmitAction($action: String!, $signature: String!, $address: String!) {
    submitAction(action: $action, signature: $signature, address: $address)
    {
        code
        error
        message
        __typename
    }
}
"""
    variables = {
        "signature": signed_message,
        "address": address,
        "action": message,
    }
    response = gql.send_mutation(query, variables)
    return response
