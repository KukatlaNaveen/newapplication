import json
from storage import Storage

class User:
    def __init__(self):
        self.storage = Storage("users.json")
        self.current_user = None

        try:
            self.__users = self.storage.load()
        except:
            self.__users = {}

        if not isinstance(self.__users, dict):
            self.__users = {}

    def register(self, username, password):
        if username in self.__users:
            print("User already exists")
            return False

        self.__users[username] = password
        self.storage.save(self.__users)
        print("Registration successful")
        return True

    def login(self, username, password):
        if username in self.__users and self.__users[username] == password:
            self.current_user = username
            print("Login successful")
            return True

        print("Invalid login")
        return False