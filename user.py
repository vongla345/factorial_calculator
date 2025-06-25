from typing import Optional, List, Tuple

class User:
    """
    Implementation of User used for login page
    
    Attrs:
        username (str): username of the user
        password (str): password of the user
    """
    
    def __init__(self, username: str, password: str) -> None:
        """
        Init infor for user

        Args:
            username (str): username of the user
            password (str): password of the user
        """
        self.username = username
        self.password = password
        
    def get_username(self) -> str:
        """
        get username of the user

        Returns:
            str : username of the user
        """
        return self.username
    
    def check_password(self, password: str) -> bool:
        """
        check if the given password is correct or not

        Args:
            password (str): password which user type in

        Returns:
            bool: true if password which user type 
                    is matched with password stored
        """
        return self.password == password


class UserList:
    """
    Implementaion for list of users
    
    Attrs:
        user_list (List[User]): list used for store user's infor
    """
    
    def __init__(self, link_user_file: str) -> None:
        """
        Init infor for UserList by loading file .txt

        Args:
            link_user_file (str): link of file .txt store infor of users
        """
        with open (link_user_file, "r") as f:
            users = [i.strip().split(" ") for i in f.readlines()]
        
        self.user_list = [User(user[0],user[1]) for user in users]
        
    def check_exist_username(self, username: str) -> Optional[User]:
        """
        check if username exist in list or not

        Args:
            username (str): username which user type in

        Returns:
            Optional[User]: return User object if username which user type in is existed,
                            None otherwise
        """ 
        for user in self.user_list:
            if username == user.get_username():
                return user
        
        return None
    
    def check_login(self, username: str, password: str) -> Tuple[bool, str]:
        """
        check if login success or not base on given username and password

        Args:
            username (str): username which user type in
            password (str): password which user type in

        Returns:
            Tuple[bool, str]: return tuple with True if login success, False otherwise
                                with information 
        """
        user = self.check_exist_username(username)
        
        if not user:
            return (False, "User not exist")
        
        if user.check_password(password):
            return (True, "Login success")
        else:
            return (False, "Wrong password")