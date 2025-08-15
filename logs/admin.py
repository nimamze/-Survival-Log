from django.contrib import admin

from .models import *

admin.site.register(Log)
admin.site.register(ZoneConnection)
admin.site.register(Zone)
admin.site.register(Puzzle)