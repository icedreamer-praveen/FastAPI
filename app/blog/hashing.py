from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=['bcrypt'], deprecated='auto')

class Hash():
    def bcrypt(password: str):
        """
        The function bcrypt takes a password string as input, hashes it using pwd_cxt, and returns the
        hashed password.
        
        :param password: The parameter `password` is a string that represents the plain text password
        that needs to be hashed using the bcrypt algorithm
        :type password: str
        :return: the hashed version of the input password using the bcrypt algorithm.
        """
        hashedPassword = pwd_cxt.hash(password)
        return hashedPassword

    def verify(hashed_password, plain_password):
        """
        The function verifies if a plain password matches a hashed password using a password context.
        
        :param hashed_password: The hashed password is a string that has been processed by a
        cryptographic hash function to produce a fixed-length string of characters that represents the
        original password in a way that is difficult to reverse. This is typically used for secure
        storage of passwords, as the original password cannot be easily retrieved from the hashed
        version
        :param plain_password: The plain_password parameter is the password entered by the user in its
        original, unencrypted form
        :return: a boolean value indicating whether the plain password matches the hashed password. If
        the passwords match, the function will return True, otherwise it will return False.
        """
        return pwd_cxt.verify(plain_password, hashed_password)