import graphene
from .mutations import CreateUserMutation, UpdateUserMutation, DeleteUserMutation, UserLoginMutation
from .queries import UserQuery


class Mutation(graphene.ObjectType):
    create_user = CreateUserMutation.Field()
    update_user = UpdateUserMutation.Field()
    delete_user = DeleteUserMutation.Field()
    login = UserLoginMutation.Field()


class Query(UserQuery):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
