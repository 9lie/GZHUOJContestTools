import requests
import json

HEADERS = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36'
}
COOKIES = {}

URL = 'http://121.196.96.104:11087/'
PROFILE = URL + 'api/profile'
LOGIN_URL = URL + 'api/login'
CONTEST_SUBMISSIONS_URL = URL + 'api/contest_submissions'


def init():
    '''
    get csrftoken
    '''
    global COOKIES
    res = requests.get(PROFILE)
    COOKIES = res.cookies
    HEADERS['X-CSRFToken'] = res.cookies['csrftoken']


def login(username, password):
    global COOKIES
    res = requests.post(LOGIN_URL, headers=HEADERS, cookies=COOKIES, json={
        'username': username,
        'password': password
    })
    assert res.status_code == 200
    COOKIES = res.cookies


def getStatus(cid, limit=30):
    '''
    get first page results
    limit: max number of results
    '''
    res = requests.get(CONTEST_SUBMISSIONS_URL, cookies=COOKIES, params={
        'contest_id': str(cid),
        'limit': limit
    })
    assert res.status_code == 200
    results = json.loads(res.text)

    return list(map(lambda result: {'userName': result['user_id'], 'problemID': result['problem']}, results['data']['results'])), results['data']['total']


if __name__ == '__main__':
    init()
    login('username', 'password')
    res = getStatus(1, 3)
    print(res)
