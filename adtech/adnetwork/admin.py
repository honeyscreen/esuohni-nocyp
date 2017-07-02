from django.contrib import admin

from .models import *

admin.site.register(User)
admin.site.register(Campaign)
admin.site.register(Click)
admin.site.register(Conversion)