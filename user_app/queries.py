import graphene
from graphql import GraphQLError

from .models import CustomerUser
from .object_type import UserType


class UserQuery(graphene.ObjectType):
    all_users = graphene.List(UserType)
    get_user = graphene.Field(UserType, id=graphene.Int())

    def resolve_all_users(self, info, **kwargs):
        return CustomerUser.objects.all()


    def resolve_get_user(self, info, **kwargs):
        try:
            user = CustomerUser.objects.filter(id=kwargs.get('id')).last()
            if user:
                return user
            else:
                return GraphQLError("User does not exist")
            
        except Exception as e:
            return GraphQLError(str(e))
