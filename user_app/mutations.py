import graphene
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from graphql import GraphQLError
from graphql_jwt.shortcuts import create_refresh_token, get_token

from .models import CustomerUser
from .object_type import UserType


class CreateUserMutation(graphene.Mutation):
    data = graphene.Field(UserType)
    message = graphene.String()

    class Arguments:
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        username = graphene.String(required=True)
        email = graphene.String(required=True)
        password = graphene.String(required=True)
        confirm_password = graphene.String(required=True)
        mobile = graphene.String(required=False)
        address = graphene.String(required=False)

    def mutate(self, info, first_name, last_name, username, email, password, confirm_password, mobile=None, address=None):
        try:
            if password != confirm_password:
                return CreateUserMutation(data=None, message="Wrong password")

            user = CustomerUser.objects.filter(email=email).last()
            if user:
                return CreateUserMutation(data=None, message="User already exists")

            user = CustomerUser(first_name=first_name, last_name=last_name, username=username, email=email, mobile=mobile, address=address)
            user.set_password(password)
            user.save()
            return CreateUserMutation(data=user, message="User created")
        
        except Exception as e:
            return GraphQLError(str(e))


class UpdateUserMutation(graphene.Mutation):
    data = graphene.Field(UserType)
    message = graphene.String()
    class Arguments:
        id = graphene.ID(required=True)
        first_name = graphene.String(required=False)
        last_name = graphene.String(required=False)
        mobile = graphene.String(required=False)
        address = graphene.String(required=False)

    def mutate(self, info, id, first_name=None, last_name=None, mobile=None, address=None):
        try:
            customer = CustomerUser.objects.filter(id=id).last()
            if not customer:
                return UpdateUserMutation(data=None, message="User does not exist")

            if first_name:
                customer.first_name = first_name

            if last_name:
                customer.last_name = last_name

            if mobile:
                customer.mobile = mobile

            if address:
                customer.address = address

            customer.save()
            return UpdateUserMutation(data=customer, message="User details updated")
        
        except Exception as e:
            return GraphQLError(str(e))


class DeleteUserMutation(graphene.Mutation):
    message = graphene.String()

    class Arguments:
        id = graphene.ID(required=True)

    def mutate(self, info, id):
        try:
            customer = CustomerUser.objects.filter(id=id).last()
            if not customer:
                return DeleteUserMutation(message="User does not exist")

            customer.delete()

            return DeleteUserMutation(message="User deleted")
        
        except Exception as e:
            return GraphQLError(str(e))


class UserLoginMutation(graphene.Mutation):
    data = graphene.Field(UserType)
    access_token = graphene.String()
    refresh_token = graphene.String()
    message = graphene.String()
    class Arguments:
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    def mutate(self, info, email, password):
        try:
            customer = CustomerUser.objects.filter(email=email).last()
            if customer:
                user = authenticate(username=customer.username, password=password)
                if user is not None:
                    login(info.context, user)
                    token = get_token(user)
                    refresh_token = create_refresh_token(user)

                    return UserLoginMutation(data=customer, access_token=token, refresh_token=refresh_token, message="Login successfully")

            else:
                return UserLoginMutation(data=None, access_token=None, refresh_token=None, message="Invalid email or password")

        except Exception as e:
            return GraphQLError(str(e))