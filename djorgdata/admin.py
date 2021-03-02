from django.contrib import admin
from organizations.models import (Organization, OrganizationUser, OrganizationOwner)
from djorgdata.forms import AccountUserForm
from djorgdata.models import Account, AccountUser


class AccountUserAdmin(admin.ModelAdmin):
    form = AccountUserForm


admin.site.unregister(Organization)
admin.site.unregister(OrganizationUser)
admin.site.unregister(OrganizationOwner)
admin.site.register(Account)
admin.site.register(AccountUser, AccountUserAdmin)
