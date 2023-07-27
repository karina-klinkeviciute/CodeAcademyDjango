import factory
from django.contrib.auth.models import User


class RandomUserFactory(factory.Factory):
    class Meta:
        model = User

    first_name = factory.Faker('first_name')
    last_name = "Smith"

# user = RandomUserFactory()

# print(user.first_name)
