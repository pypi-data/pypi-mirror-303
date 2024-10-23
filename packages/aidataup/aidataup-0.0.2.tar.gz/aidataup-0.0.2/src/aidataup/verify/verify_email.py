import re

def verify_email(email):
    # Regular expression for validating an Email
    regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

    # Remove any leading/trailing whitespaces and convert to lowercase
    if email is not None:
        email_cleansing = email.strip().lower()
    else:
        return False

    # Remove common leading strings that are not part of the email
    prefixes = ["e-mail:", "email:"]
    for prefix in prefixes:
        if email_cleansing.startswith(prefix):
            email_cleansing = email_cleansing[len(prefix):]

    # Remove non-ASCII characters (including Thai characters)
    email_cleansing = ''.join(char for char in email_cleansing if ord(char) < 128)

    # Check for the presence of '@' symbol
    if email_cleansing.count('@') != 1:
        return False

    # Remove trailing dots before the domain part
    local, domain = email_cleansing.split('@')
    local = local.rstrip('.')

    # Apply regular expression to remove invalid characters
    local = re.sub(r"[^a-zA-Z0-9_.+-]", "", local)
    
    email_cleansing = local + '@' + domain

    # Validate email format using regex
    if re.match(regex, email_cleansing):
        return True
    else:
        return False