from django.contrib import admin
from .models import *

admin.site.register(UUIDUser)
admin.site.register(Score)
admin.site.register(Word)
admin.site.register(Match)