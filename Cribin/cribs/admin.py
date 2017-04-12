# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Crib
from .models import Guest

admin.site.register(Crib)
admin.site.register(Guest)
# Register your models here.
