from graphene_django import DjangoObjectType

from .models import CustomerUser


class UserType(DjangoObjectType):
    class Meta:
        model = CustomerUser
        fields = '__all__'
        exclude_fields = ('password',)
