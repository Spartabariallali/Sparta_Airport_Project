import hashlib, binascii, os

def user_check(testing):
    new_user_check = input("If you already have a username please press enter, otherwise enter 1: ")
    if new_user_check == "":
        existing_user = input("Please enter your username: ")
        # get username and hash password from SQL
        returned_password = testing
        if True:
            # username returned testing password
            password_attempts = 3
            while password_attempts >= 0:
                user_password = input("Please enter your password: ")
                if verify_password(returned_password, user_password):
                    print("Welcome")
                    return "Validated"
                else:
                    if password_attempts == 0:
                        print("Account locked.  Please contact your system administrator")
                        return "Password failed"
                    else:
                        print(f"Password incorrect. {password_attempts} attempts remaining. Please try again")
                        password_attempts -= 1
        else:
            result = create_user()
            return result
    else:
        result = create_user()
        return result

def create_user():
    new_user = input("Please enter your new username: ")
    new_password = input("Please enter your password: ")
    new_password_hash = hash_password(new_password)
    # store new user and hashed password in SQL
    print("Thank you! You can now log in!")
    return "New user created"


def hash_password(password):
    """Encodes a provided password in a way that is safe to store on a database or file"""
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                  salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')


def verify_password(stored_password, provided_password):
    """Given an encoded password and a plain text one is provided by the user,
    it verifies whether the provided password matches the encoded (and thus saved) one."""
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512',
                                  provided_password.encode('utf-8'),
                                  salt.encode('ascii'),
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password


testing = hash_password("password1")
user_check(testing)