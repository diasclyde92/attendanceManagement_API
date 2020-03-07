import unittest
from app.main.service.users_service import *
# from mongoengine import *


# disconnect()
# connect('test_cases')

# Insert users

data = {
  "username": "tfefe15",
  "name": {
    "firstName": "string",
    "lastName": "string"
  },
  "email": "string@opspl.com",
  "password": "test123"
}


class TestUsers(unittest.TestCase):

    def test_insert_users(self):
        response = insert_users(data)
        print(response)
        self.assertEqual(response[1], 201)


if __name__ == '__main__':
    unittest.main()