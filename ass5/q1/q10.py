#Email Validation with Custom Exception
import re

class InvalidEmailError(Exception):
    pass

try:
    email = input("Enter email: ")
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    if not re.match(pattern, email):
        raise InvalidEmailError("Invalid email format.")

    print("Valid email.")

except InvalidEmailError as e:
    print("Error:", e)
