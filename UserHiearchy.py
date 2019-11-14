import io
import json
import sys

"""Represents hiearchy of users and their roles

@author Mohamed Osman
"""
class UserHiearchy:
    def __init__(self):
        self.users = None
        self.roles = None

    """Sets users passed in from the json file into a users dictionary in our class

    :param users: list of dictionaries, where each dictionary is a user
    """
    def setUsers(self, users):
        # Raise an exception if passed in users are empty
        if not users or not isinstance(users, list):
            raise Exception("No users to be added.")
        self.users = users


    """Sets roles passed in from the json file by creating a key/value dictionary
    of roles and their subordinates

    :roles: list of dictionaries, where each dictinary is a role
    """
    def setRoles(self, roles):
        # Raise an exception if no passed in roles are empty
        if not roles or not isinstance(roles, list):
            raise Exception("No roles to be added.")

        # This dictionary will represent a dictionary where each key is the "Id" and
        # each value is a dictionary that holds the value for each role and also
        # a list of subordinates
        roleDic = {}

        # Iterate over passed in roles to populate the dictionary with the roles 
        # and initialize an empty list of subordinates
        for role in roles:
            roleDic[role["Id"]] = { "role": role, "subordinates": [] }

        # Iterate over passed in roles to populate the subordinates list
        for role in roles:
            parent = role["Parent"]

            # Iterate from youngest child to parent for each role to
            # append subordinates to the list
            while parent is not 0:
                parentRole = roleDic[parent]
                parentRole["subordinates"].append(role["Id"])
                parent = parentRole["role"]["Parent"]

        self.roles = roleDic


    """Gets subordinates of the passed in id

    :id: id of the role we would like to get its subordinates
    """
    def getSubordinates(self, id):
        # Iterate over users to find the user with the passed in id
        wantedUser = next((user for user in self.users if user["Id"] == id), None)

        # Raise exception if entered id does not map to a user in our list
        if not wantedUser: raise Exception("User does not exist.")

        # Subordinates of wanted user
        subordinates = self.roles[wantedUser["Role"]]["subordinates"]

        # This list will be populated below which will hold all the subordinates
        # of the entered id
        subordinatesList = []
        
        # Iterate over users and append to the list all the users with that specific
        # id
        for user in self.users:
            if user["Role"] in subordinates:
                subordinatesList.append(user)

        return subordinatesList

if __name__ == "__main__":
    with io.open('users.json', encoding='utf-8') as users_file, io.open('roles.json', encoding='utf-8') as roles_file:
        users = json.loads(users_file.read())
        roles = json.loads(roles_file.read())

    UserHiearchy = UserHiearchy()
    UserHiearchy.setUsers(users)
    UserHiearchy.setRoles(roles)
    userId = int(sys.argv[1])
    print(UserHiearchy.getSubordinates(userId))