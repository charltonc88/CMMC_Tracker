# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import Organization
from .models import Control

# Register your models here.

admin.site.register(Organization)
admin.site.register(Control)