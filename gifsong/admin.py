from django.contrib import admin
from gifsong.models import gifsong

class gifsongAdmin(admin.ModelAdmin):
    list_display = ('gif',)

    def gif(self, obj):
        return '<img style="width:100px;height:75px;" src="http://%s"/>' % (obj.image_url)
    gif.allow_tags = True
    gif.short_description = 'Gif Used'

admin.site.register(gifsong, gifsongAdmin)
