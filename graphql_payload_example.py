
# payload for create user (copy and past in postman graphql body)
"""
# Payload example:
mutation CreateUser {
    createUser(
        email: "example@gmail.com"
        firstName: "example"
        lastName: "test"
        password: "Test@1234"
        confirmPassword: "Test@1234"
        username: "example"
        address: "indore madhya pradesh"
        mobile: "0123456789"
    ) {
        message
        data {
            id
            isSuperuser
            username
            firstName
            lastName
            email
            mobile
            address
        }
    }
}

"""

"""
Response example:
{
    "data": {
        "createUser": {
            "message": "User created",
            "data": {
                "id": "9",
                "isSuperuser": false,
                "username": "example",
                "firstName": "example",
                "lastName": "test",
                "email": "example@gmail.com",
                "mobile": "0123456789",
                "address": "indore madhya pradesh"
            }
        }
    }
}


"""


# Query for get all user
"""
# Payload example:
query AllUsers {
    allUsers {
        id
        username
        firstName
        lastName
        email
        mobile
        address
    }
}

"""


"""
Response example:
{
    "data": {
        "allUsers": [
            {
                "id": "4",
                "lastLogin": null,
                "isSuperuser": false,
                "username": "test",
                "firstName": "sonu",
                "lastName": "test",
                "email": "test2@gmailcom",
                "isStaff": false,
                "isActive": true,
                "dateJoined": "2024-01-01T18:28:20.822593+00:00",
                "mobile": "12345678",
                "address": "indore"
            },
            {
                "id": "6",
                "lastLogin": null,
                "isSuperuser": false,
                "username": "Test4",
                "firstName": "Test4",
                "lastName": "Test4",
                "email": "Test4@gmail.com",
                "isStaff": false,
                "isActive": true,
                "dateJoined": "2024-01-01T18:41:13.489028+00:00",
                "mobile": null,
                "address": null
            },
            {
                "id": "7",
                "lastLogin": "2024-01-08T09:20:44.840264+00:00",
                "isSuperuser": false,
                "username": "test12345",
                "firstName": "test",
                "lastName": "tw",
                "email": "test@gmail.com",
                "isStaff": false,
                "isActive": true,
                "dateJoined": "2024-01-08T06:59:15.321123+00:00",
                "mobile": null,
                "address": null
            },
            {
                "id": "8",
                "lastLogin": null,
                "isSuperuser": false,
                "username": "example",
                "firstName": "example",
                "lastName": "test",
                "email": "example@gmail.com",
                "isStaff": false,
                "isActive": true,
                "dateJoined": "2024-01-08T09:40:13.449544+00:00",
                "mobile": "0123456789",
                "address": "indore madhya pradesh"
            },
            {
                "id": "9",
                "lastLogin": null,
                "isSuperuser": false,
                "username": "example1",
                "firstName": "example",
                "lastName": "test",
                "email": "example1@gmail.com",
                "isStaff": false,
                "isActive": true,
                "dateJoined": "2024-01-08T09:50:47.255468+00:00",
                "mobile": "0123456789",
                "address": "indore madhya pradesh"
            }
        ]
    }
}
"""





