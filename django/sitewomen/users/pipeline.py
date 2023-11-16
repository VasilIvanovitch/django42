from django.contrib.auth.models import Group


def new_users_handler(backend, user, response, *args, **kwargs):
    group = Group.objects.filter(name='social')
    if len(group):
        # print(f'Creating new {group[0]}')
        user.groups.add(group[0])
