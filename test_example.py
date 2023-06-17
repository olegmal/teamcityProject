import pytest


def check_passwd(username, password, min_length=10, check_username=True):

    if len(password) < min_length:
        print("Password is too short")
        return False
    elif check_username and username in password:
        print("Password contain user name")
        return False
    else:
        print(f"Password for user {username} is correct")
        return True


def test_password_min_length():
    assert check_passwd('user', '54321', min_length=4) == True
    assert check_passwd('user', '12345', min_length=7) == False
    assert check_passwd('user', 'admin1', min_length=4) == True