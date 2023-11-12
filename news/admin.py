from django.contrib import admin
from news.models import newsApp

class newsApp_admin(admin.ModelAdmin):
    list_display = ('news_title','news_image','news_desc')

admin.site.register(newsApp,newsApp_admin)

