import bcrypt


def hashing(userInfo: str) -> str:
    """
    Hashes user information using the bcrypt library.

    Args:
        userInfo (str): The user information to hash

    Returns:
        str: The hashed version of the user information.
    """
    # Convert the input string to bytes
    userInfoBytes = userInfo.encode('utf-8')

    # Generate a salt
    salt = bcrypt.gensalt()

    # Hash the user information with the salt
    hashedInfo = bcrypt.hashpw(userInfoBytes, salt)

    # Return the hashed info as a string
    return hashedInfo.decode('utf-8')

def verifyHash(userInfo: str, hashedInfo: str) -> bool:
    """
    Verifies if the user information matches the hashed value.

    Args:
        user_info (str): The user information to verify.
        hashed_info (str): The hashed value to compare against.

    Returns:
        bool: True if the input matches the hash, False otherwise.
    """
    return bcrypt.checkpw(userInfo.encode('utf-8'), hashedInfo.encode('utf-8'))

# Example usage
if name == "main":

    # hashing
    user_info = "test info"
    hashed_info = hashing(user_info)
    print(type(hashed_info))
    print(f"Hashed Information: {hashed_info}")

    # verify
    user_info = "test password"
    hashed_info = hashing(user_info)

    # Test verification
    is_valid = verifyHash("test password", hashed_info)
    print(f"Verification Result: {is_valid}")  # Output: True