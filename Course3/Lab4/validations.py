import re

def validate_user(username, minlen):
    """
    Checks if the received username matches the required conditions.
    :param username: The username to validate.
    :param minlen: Minimum length for the username.
    :return: True if the username is valid, False otherwise.
    """
    if not isinstance(username, str):
        raise TypeError("username must be a string")
    if minlen < 1:
        raise ValueError("minlen must be at least 1")

    # Usernames can't be shorter than minlen
    if len(username) < minlen:
        return False
    # Usernames can only use letters, numbers, dots, and underscores
    if not re.match(r'^[a-z0-9._]*$', username):
        return False
    # Usernames can't begin with a number or dot
    if username[0].isdigit() or username[0] == '.' or username[0] == '_' :
        return False

    return True

# Example usage:
if validate_user("my_username123", 5):
    print("Valid username!")
else:
    print("Invalid username.")

print(validate_user("blue.kale", 3)) # True
print(validate_user(".blue.kale", 3)) # Currently True, should be False
print(validate_user("red_quinoa", 4)) # True
print(validate_user("_red_quinoa", 4)) # Currently True, should be False

