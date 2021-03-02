from organizations.models import Organization, OrganizationUser
from django.db import models


class Account(Organization):
    class Meta:
        proxy = True


class AccountUser(OrganizationUser):
    """
    The AccountUser model only has three fields: a foreign key to the organization, a foreign key to the user, and \
    since this is our default class, a Boolean field for admins.
    """
    class Meta:
        proxy = True


class ServiceProvider(Organization):
    """Now this model has a name field and a slug field"""
    url = models.URLField()



