'''
Manual test:

curl -i -X POST -H 'Content-Type:application/json' -d '{"name":"Admins"}' localhost:8080/groups
curl -i -X POST -H 'Content-Type:application/json' -d '{"name":"Testers"}' localhost:8080/groups

curl localhost:8080/groups
curl localhost:8080/groups/1

#curl -v -X PUT -H "Content-Type: text/uri-list" -d "http://localhost:8080/groups/1" http://localhost:8080/users/1/groups
#curl -X PUT -H "Content-Type: application/json" -d '{"_links":{"groups":{"href":"http://localhost:8080/groups/1"}}}' http://localhost:8080/users/1/groups

curl -i -X POST -H 'Content-Type:application/json' -d '{"email":"fb@example.com","firstName":"Frodo","lastName":"Baggins"}' localhost:8080/users
curl -i -X POST -H 'Content-Type:application/json' -d '{"email":"fb@example.com","firstName":"Frodo","lastName":"Baggins","groups":["http://localhost:8080/groups/1","http://localhost:8080/groups/2"]}' localhost:8080/users

curl localhost:8080/users
curl localhost:8080/users/1

'''
