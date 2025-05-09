users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"}
]

def add_user(user):
    users.append(user)

def delete_user(user_id):
    global users
    users = [user for user in users if user["id"] != user_id]

def update_user(user_id, name=None, email=None):
    for user in users:
        if user["id"] == user_id:
            if name:
                user["name"] = name
            if email:
                user["email"] = email
            return

def get_user(user_id):
    for user in users:
        if user["id"] == user_id:
            return user
    return None
