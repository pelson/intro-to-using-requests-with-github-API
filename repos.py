from pathlib import Path
from pprint import pprint

import requests


def api_token():
    token_file = Path('token.txt')
    if not token_file.exists():
        raise IOError('Please create a token at github.com, and save it in {}'.format(token_file))

    token = token_file.read_text().strip()
    return token


def main():
    token = api_token()
    headers = {'Authorization': 'token {}'.format(token)}

    API_URL = 'https://api.github.com'

    target = '/user/repos'
    resp = requests.get('{}{}'.format(API_URL, target),
                        headers=headers)
    content = resp.json()
    pprint(content[:3])


if __name__ == '__main__':
    main()
