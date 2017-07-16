# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import MyUser


class MyUserAdmin(admin.ModelAdmin):
	class Meta:
		model = MyUser 
		fields = ('user_id', 'area', 'tarrif')

admin.site.register(MyUser, MyUserAdmin)



