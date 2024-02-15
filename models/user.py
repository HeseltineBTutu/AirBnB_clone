"""defines class User"""
from .base_model import BaseModel


class User(BaseModel):
    """
    Defines the User class, representing a user entity in the system.

    Attributes:
        email (str): The email address associated with the user. Default is an empty string.
        password (str): The password of the user. Default is an empty string.
        first_name (str): The first name of the user. Default is an empty string.
        last_name (str): The last name of the user. Default is an empty string.

    Usage:
        This class is used to represent user entities within the system.
        Users can have attributes such as email, password, first name,
        and last name, which can be set and accessed directly using dot notation.

    Example:
        # Creating a new user
        user1 = User()
        user1.email = "heseltinetutu@alx.com"
        user1.password = "secure_password"
        user1.first_name = "Heseltine"
        user1.last_name = "Tutu"

        # Accessing user attributes
        print(user1.email)  # Output: heseltinetutu@alx.com
        print(user1.first_name)  # Output: Heseltine
        """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
