from django.contrib import admin
from gifsong.models import gifsong

class gifsongAdmin(admin.ModelAdmin):
    pass
admin.site.register(gifsong, gifsongAdmin)
