from UserHiearchy import UserHiearchy
import unittest
import io
import json

userHiearchy = UserHiearchy()
with io.open('users.json', encoding='utf-8') as users_file, io.open('roles.json', encoding='utf-8') as roles_file:
    users = json.loads(users_file.read())
    roles = json.loads(roles_file.read())
userHiearchy.setUsers(users)
userHiearchy.setRoles(roles)

"""Test cases for UserHiearchy

@author Mohamed Osman
"""
class UserHiearchyTest(unittest.TestCase):

	def setUp(self):
		print(self.id())

	# """Test setting users correctly without any errors
	# """
	# def testSetUsersCorrectly(self):
	# 	userHiearchy.setUsers(users)

	"""Test setting users with an empty list of users
	"""
	def testSetUsersWithEmptyUsersList(self):
		with self.assertRaises(Exception) as context:
			userHiearchy.setUsers([])
		self.assertTrue("No users to be added!" in context.exception)

	"""Test setting users with users of type dictionary NOT list
	"""
	def testSetUsersWithIncorrectTypeOfDataStructure(self):
		with self.assertRaises(Exception) as context:
			userHiearchy.setUsers(dict)

		self.assertTrue("No users to be added!" in context.exception)

	"""Test setting roles correctly without any errors
	"""
	def testSetRolesCorrectly(self):
		userHiearchy.setRoles(roles)

	"""Test setting users with an empty list of roles
	"""
	def testSetRolesWithEmptyRolesist(self):
		with self.assertRaises(Exception) as context:
			userHiearchy.setRoles([])

		self.assertTrue("No roles to be added!" in context.exception)

	"""Test setting users with users of type dictionary NOT list
	"""
	def testSetRolesWithIncorrectTypeOfDataStructure(self):
		with self.assertRaises(Exception) as context:
			userHiearchy.setUsers(dict)

		self.assertTrue("No users to be added!" in context.exception)

	"""Test getting subordinates with correct id value
	"""
	def testGetSubordinates(self):
		subordinates = userHiearchy.getSubordinates(1)

		self.assertEqual(subordinates[0]["Role"], 4)
		self.assertEqual(subordinates[0]["Id"], 2)
		self.assertEqual(subordinates[0]["Name"], "Emily Employee")


	"""Test getting user id that has no subordinates
	"""
	def testGettingEmptySubordinates(self):
		subordinates = userHiearchy.getSubordinates(2)

		self.assertEqual(subordinates, "Emily Employee does not have any subordinates.")


	"""Test getting subordinates with an id value that does not exist
	"""
	def testGetSubordinatesWithIncorrectId(self):
		with self.assertRaises(Exception) as context:
			userHiearchy.getSubordinates(10)

		self.assertTrue("User does not exist!" in context.exception)

	"""Test getting subordinates by entering an id of type string
	"""
	def testGetSubordinatesWithStringId(self):
		with self.assertRaises(Exception) as context:
			userHiearchy.getSubordinates("Not a number")

		self.assertTrue("Entered id must be a number!" in context.exception)

if __name__ == '__main__':
    unittest.main()