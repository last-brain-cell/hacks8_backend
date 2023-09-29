def indivisual_serial(users):
    return {
        "id" : str(users["_id"]),
        "username": str(users["username"]),
        "password": str(users["password"]),
        "access_level": int(users["access_level"])
    }

def list_serial(users):
    return [indivisual_serial(user) for user in users]