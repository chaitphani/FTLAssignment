from Ftlapp.models import User
from django.core.management.base import BaseCommand
from faker import Faker

faker = Faker()
class Command(BaseCommand):
    help = 'Create random users'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of users to be created')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        for i in range(total):
            # import ipdb; ipdb.set_trace();
            users_obj = User.objects.create(name=faker.name(), address=faker.address())
            # print('w012a3c'+str(users_obj.id))
            users_obj.user_id = 'W012A3C' + str(users_obj.id)
            users_obj.save()
            # print(users_obj.user_id)





