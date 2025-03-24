import re
regex = r'\b[A-Za-z0-9._+]+@[A-Za-z0-9]+\.[A-Z|a-z]{2,7}\b'


def email_checking(func):
    def wrapper(*args, **kwargs):
        email = func(*args, **kwargs)
        if re.fullmatch(regex, email):
            return True
        else:
            return False

    return wrapper
