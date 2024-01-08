# your_app/tests/test_mutations.py
import json
from django.test import TestCase
from graphene.test import Client
from ..models import CustomerUser
from ..schemas import schema


class CreateUserMutationTestCase(TestCase):
    def setUp(self):
        # Set up a test GraphQL client
        self.client = Client(schema)

    def test_create_user_mutation(self):
        # Define the input data for the mutation
        mutation_input = {
            'first_name': 'John',
            'last_name': 'Doe',
            'username': 'john_doe',
            'email': 'john.doe@example.com',
            'password': 'password123',
            'confirm_password': 'password123',
            'mobile': '1234567890',
            'address': 'Test Address',
        }

        # Create a mutation query string
        mutation_query = f'''
            mutation {{
                createUser(
                    firstName: "{mutation_input['first_name']}",
                    lastName: "{mutation_input['last_name']}",
                    username: "{mutation_input['username']}",
                    email: "{mutation_input['email']}",
                    password: "{mutation_input['password']}",
                    confirmPassword: "{mutation_input['confirm_password']}",
                    mobile: "{mutation_input['mobile']}",
                    address: "{mutation_input['address']}"
                ) {{
                    data {{
                        id
                        firstName
                        lastName
                        username
                        email
                        mobile
                        address
                    }}
                    message
                }}
            }}
        '''

        # Execute the mutation
        response = self.client.execute(mutation_query)

        # Verify the response
        self.assertIn('createUser', response['data'])
        user_data = response['data']['createUser']['data']
        self.assertIsNotNone(user_data)
        self.assertEqual(user_data['firstName'], mutation_input['first_name'])
        self.assertEqual(user_data['lastName'], mutation_input['last_name'])
        self.assertEqual(user_data['username'], mutation_input['username'])
        self.assertEqual(user_data['email'], mutation_input['email'])
        self.assertEqual(user_data['mobile'], mutation_input['mobile'])
        self.assertEqual(user_data['address'], mutation_input['address'])

        # Verify the message
        self.assertEqual(response['data']['createUser']['message'], 'User created')

        # Verify that the user is actually created in the database
        user = CustomerUser.objects.get(email=mutation_input['email'])
        self.assertIsNotNone(user)
        self.assertEqual(user.first_name, mutation_input['first_name'])
        # Add more assertions as needed

