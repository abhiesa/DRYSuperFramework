'''
Manual test:

curl -i -X POST -H 'Content-Type:application/json' -d '{"name":"Admins"}' localhost:8080/groups
curl -i -X POST -H 'Content-Type:application/json' -d '{"name":"Testers"}' localhost:8080/groups

curl localhost:8080/groups
curl localhost:8080/groups/1

curl -i -X POST -H 'Content-Type:application/json' -d '{"email":"fb@example.com","firstName":"Frodo","lastName":"Baggins"}' localhost:8080/users
curl -i -X POST -H 'Content-Type:application/json' -d '{"email":"fb@example.com","firstName":"Frodo","lastName":"Baggins","groups":["http://localhost:8080/groups/1","http://localhost:8080/groups/2"]}' localhost:8080/users

curl localhost:8080/users
curl localhost:8080/users/1

#curl -v -X PUT -H "Content-Type: text/uri-list" -d "http://localhost:8080/groups/1" http://localhost:8080/users/1/groups
#curl -X PUT -H "Content-Type: application/json" -d '{"_links":{"groups":{"href":"http://localhost:8080/groups/1"}}}' http://localhost:8080/users/1/groups

'''

import json

import requests

HEADERS_JSON = {'Content-Type': 'application/json'}

def printj(j):
    print(json.dumps(j, indent=4))

def test_all():
    requests.post('http://localhost:8080/groups', headers=HEADERS_JSON, data='{"name":"Admins"}')
    requests.post('http://localhost:8080/groups', headers=HEADERS_JSON, data='{"name":"Testers"}')

    rj = requests.get('http://localhost:8080/groups/').json()
    groups = rj['_embedded']['groups']

    groups_hrefs = []
    for group in groups:
        groups_hrefs.append(group['_links']['group']['href'])

    user_json = {
        "email": "fb@example.com",
        "firstName": "Frodo",
        "lastName": "Baggins",
        "groups": groups_hrefs
    }

    rj = requests.post('http://localhost:8080/users', headers=HEADERS_JSON, data=json.dumps(user_json)).json()
    user_href = rj['_links']['user']['href']

    # UPDATE

    user_json = {
        "email": "fb2@example.com",
        "firstName": "Frodo",
        "lastName": "Baggins",
        "groups": groups_hrefs[:-1]
    }

    r = requests.put(user_href, headers=HEADERS_JSON, data=json.dumps(user_json))
    print r.text


if __name__ == '__main__':
    test_all()
