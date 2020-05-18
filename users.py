import json
import datetime


class User():
    """
    """

    def __init__(self, username: str, userpass: str, user_db='users.json', delivery_history='history.json'):
        """
        """

        self.username = str(username)
        self.userpass = str(userpass)
        self.user_db = str(user_db)

    def register_user(self, userdata: dict, userpass: str) -> bool:
        """
        """

        user_db=self.user_db
        username=self.username

        def __check_duplicate(user_db: str, username: str) -> bool:
            """
            """

            try:
                with open(user_db, 'r') as db:
                    users = json.loads(db.read())

                if username in users.keys():
                    return False
                else:
                    return True
            except (FileNotFoundError, PermissionError) as read_err:
                print('FAILED TO READ USERS DATABASE!') # To be replaced w/ logging.
                raise

        if __check_duplicate(username=username, user_db=self.user_db) is True:
            try:
                with open(user_db, 'r') as db:
                    users=json.loads(db.read())
                with open(user_db, 'w') as db:
                    users[username] = userdata
                    json.dump(users, db)
            except (FileNotFoundError, PermissionError) as read_err:
                print('FAILED TO READ USERS DATABASE!') # To be replaced w/ logging.
                raise
        else:
            print('Username is already exists!') # To be replaced w/ logging.
            raise ValueError('Username is already exists!')

    def _check_user(self, username: str, userpass: str) -> bool:
        """
        """

        user_db=self.user_db

        try:
            with open(user_db, 'r') as db:
                users = json.loads(db.read())

            for user in users:
                print('{}: -> '.format(user))
                for userdata in users[user]:
                    print('\t {} -> {}'.format(userdata, users[user][userdata]))
            return None
        except (FileNotFoundError, PermissionError) as read_err:
            print('FAILED TO READ USERS DATABASE!') # To be replaced w/ logging.
            raise

    def user_bio(self, username: str, userpass: str) -> dict:
        """
        """

        return None

    def user_history(self, delivery_history: str, username: str, userpass: str) -> dict:
        """
        """

        try:
            with open(delivery_history, 'r') as hist:
                history = json.loads(hist.read())
            return history[username]
        except (FileNotFoundError, PermissionError) as read_err:
            print('FAILED TO READ USERS DATABASE!') # To be replaced w/ logging.
            raise


class Customer(User):
    """
    """

    def __init__(self):
        """
        """

        pass


class Сourier(User):
    """
    """

    def __init__(self):
        """
        """

        pass


### TEST AREA === TEST AREA === TEST AREA === TEST AREA === TEST AREA === TEST AREA === TEST AREA === TEST AREA === TEST AREA

user = User(username='+70000000000', userpass='NOT_NEEDED')

# Test 1: register new user:

first_name = str(input('What is your first name?'))
last_name= str(input('What is your last name?'))
location= str(input('Where are you now?'))

userdata = {
    'first_name': first_name,
    'last_name': last_name,
    'location': location
}

user.register_user(userdata=userdata, userpass='NOT_NEEDED') # Actual register

user._check_user('+70000000000', 'NOT_NEEDED') # Check it
