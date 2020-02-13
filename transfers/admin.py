from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import *


class UserProfileInline(admin.StackedInline):
	model = UserProfile
	can_delete = False
	verbose_name_plural = 'UserProfile'
	fk_name = 'user'


class CustomUserAdmin(UserAdmin):
	inlines = (UserProfileInline,)

	def get_inline_instances(self, request, obj=None):
		if not obj:
			return []
		return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(PS2TSTransfer)
admin.site.register(TS2PSTransfer)
admin.site.register(DeadlineModel)
