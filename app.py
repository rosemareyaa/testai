def login(user, password):
    if not user or not password:
        return False

    return user == "admin" and password == "1234"
