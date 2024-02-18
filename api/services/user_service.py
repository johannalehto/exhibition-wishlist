from sqlalchemy import text
from werkzeug.security import check_password_hash, generate_password_hash

from api.db import db


def check_existing_username(username):
    sql = text("SELECT username FROM users WHERE username=:username")
    result = db.session.execute(sql, {"username": username})
    user = result.fetchone()
    return user is not None


def check_password_match(password_first, password_second):
    return password_first == password_second


def create_new_user(username, password_first, password_second, first_name):
    if check_existing_username(username):
        return False, "Username already exist"
    if not check_password_match(password_first, password_second):
        return False, "Passwords do not match"
    password = password_first
    hash_value = generate_password_hash(password)
    new_user = {
        "username": username,
        "password": hash_value,
        "first_name": first_name,
    }
    sql = text(
        """
        INSERT INTO users (username, password, first_name)
        VALUES (:username, :password, :first_name)
        """
    )
    db.session.execute(sql, new_user)
    db.session.commit()
    return True, "User created successfully"


def create_user_session(username, password):
    sql = text("SELECT id, password FROM users WHERE username=:username")
    result = db.session.execute(sql, {"username": username})
    user = result.fetchone()
    if not user:
        return False, "Invalid username"
    else:
        user_from_db = user._asdict()
        user_id, hash_value = user_from_db['id'], user_from_db['password']
        if check_password_hash(hash_value, password):
            return True, {'id': user_id}
        else:
            return False, "Invalid password"
