from pathlib import Path

import requests


def api_token():
    token_file = Path('token.txt')
    if not token_file.exists():
        raise IOError('Please create a token at github.com, and save it in {}'.format(token_file))

    token = token_file.read_text()
    return token


def main():
    token = api_token()
    print(token)
    resp = requests.get('')

if __name__ == '__main__':
    main()
