frutas = ["maçã", "banana"]

frutas.append("laranja")


config = {
    "host": "http://localhost",
    "path": "/fruits",
    "method": "GET"
}

print(config["host"])

http_methods = {401, 402, 404, 401, 400}

print(http_methods)

a_group = {1,1,2,3,5,8}
b_group = {1,2,3,4,5,6} 

print(a_group.intersection(b_group))
print(a_group - b_group)

coordinates = (10.1213, -31.2312)

print(coordinates)