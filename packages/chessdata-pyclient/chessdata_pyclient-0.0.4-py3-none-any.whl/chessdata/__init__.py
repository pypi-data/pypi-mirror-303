"""Python library for interacting with the CHESS metadata service"""

import json
import os
import requests
import warnings

URL = 'https://foxden-meta.classe.cornell.edu:8300'

def query(query, kfile=None, url='https://foxden-meta.classe.cornell.edu:8300'):
    """Search the chess metadata database and return matching records
    as JSON

    :param query: query string to look up records
    :type query: str
    :param ticket:
    :type ticket:
    :param kfile: The name of a file containing a kerberos
        ticket. Used to obtain a foxden read token with `foxden token
        create --kfile=<kfile>` CLI if needed. Defults to `None`.
    :type kfile: string
    :param url: URL of foxden service to query, defaults to value of
        `chessdata.URL` (which is, by default,
        `'https://foxden-meta.classe.cornell.edu:8300'`).
    :type url: str, optional
    :return: list of matching records
    :rtype: list[dict]
    """
    resp = requests.post(
        f'{url}/search',
        data=json.dumps(
            {
                'service_query':
                {
                    'query': query
                }
            }
        ),
        headers={
            'Authorization': f'Bearer {get_token(scope="read", kfile=kfile)}',
            'Content-Type': 'application/json'
        }
    )
    return foxden_response_records(resp)

def add(data, schema=None, kfile=None, url='https://foxden-meta.classe.cornell.edu:8300'):
    """"""
    if schema:
        data = {'Record': data, 'Schema': schema}
    resp = requests.post(
        f'{url}',
        data=json.dumps(data),
        headers={
            'Authorization': f'Bearer {get_token(scope="write", kfile=kfile)}',
            'Content-Type': 'application/json'
        }
    )
    return resp.json()

def foxden_request_data(query):
    """Return the data to include in the body of an HTTP request to
    query a foxden service.

    :param query: The user query for the foxden service
    :type query: str
    :returns: HTTP request data
    :rtype: str
    """
    return json.dumps({'service_query': {'query': query}})

def foxden_response_records(response):
    """Return the list of records contained in the JSON response from
    a foxden service.

    :param response: A JSON response to an HTTP request to a foxden
        service.
    :type response: dict
    :returns: The data records included in the response, if any.
    :rtype: list[dict]
    """
    data = response.json()
    if isinstance(data, dict):
        results = data.get('results', {})
        records = results.get('records', [])
        return records
    return data


def token_expired(token):
    """Return True if the token provided is expired, otherwise False.

    :param token: The token to validate
    :type token: str
    :returns: Token expiration status
    :rtpe: bool
    """
    from datetime import datetime
    import jwt
    try:
        token_params = jwt.decode(token, options={"verify_signature": False})
        expires = token_params.get('exp', 0)
    except:
        expires = -1
    if expires <= datetime.now().timestamp():
        return True
    return False

def get_token(scope='read', kfile=None, create=True):
    """Return a foxden token with the requested scope.

    :param scope: Token scope
    :type scope: Literal['read', 'write', 'delete']
    :param kfile: Name of file containing a valid kerberos ticket,
        defaults to None
    :type kfile: str, optional
    :returns: Foxden token
    :rtype: str
    """
    import os
    if scope.lower() == 'read':
        env_var = 'FOXDEN_TOKEN'
    elif scope.lower() == 'write':
        env_var = 'FOXDEN_WRITE_TOKEN'
    elif scope.lower() == 'delete':
        env_var = 'FOXDEN_DELETE_TOKEN'
    else:
        raise ValueError('scope must be one of "read", "write", or "delete".')

    # First, try getting valid token from environment variable
    if env_var in os.environ:
        token = os.environ[env_var]
        if not token_expired(token):
            return token

    # If environment variable doesn't have a valid token, try getting
    # it from the ~/.foxden.*.token file
    token_file = f'{os.environ.get("HOME")}/.foxden.{scope}.token'
    if os.path.isfile(token_file):
        with open(token_file) as inf:
            token = inf.read()
        if not token_expired(token):
            return token

    # If other locations did not have a valid token, create one.
    if create:
        return create_token(scope=scope, kfile=kfile)

    return None

def create_token(scope='read', kfile=None):
    """Run the `foxden token create` command to get a foxden token.

    :param scope:
    :type scope: Literal['read', 'write', 'delete']
    :param kfile: Name of file containing a valid kerberos ticket,
        defaults to None
    :type kfile: str, optional
    :returns: None
    """
    from re import search

    if scope.lower() == 'read':
        scope_param = ''
    elif scope.lower() == 'write':
        scope_param = 'write'
    elif scope.lower() == 'delete':
        scope_param = 'delete'
    else:
        raise ValueError('scope must be one of "read", "write", or "delete".')

    foxden_create_cmd = f'foxden token create {scope_param}'
    if kfile:
        foxden_create_cmd += f' --kfile={kfile}'
    with os.popen(foxden_create_cmd, 'r') as pipe:
        out = pipe.read()
    return get_token(scope=scope, kfile=kfile, create=False)
