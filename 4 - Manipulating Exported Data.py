import json

file_path = "/mongo/db_export/users.json"
new_users = []

with open(file_path, "r") as infile:
    users = json.load(infile)
    for user in users:
        # remove the object id
        del user["_id"]
        # Capitalize first name and last name
        user['firstname'] = user['firstname'].title()
        user['lastname'] = user['lastname'].title()
        # Hide passwords
        user['password'] = '********'
        new_users.append(user)

# Sort users by first name
new_users = sorted(new_users, key=lambda x: x['firstname'])

with open(file_path, "w") as outfile:
    json.dump(new_users, outfile)