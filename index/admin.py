from django.contrib import admin
from .models import *

admin.site.register(Contact)
class CatAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
class BlogAdmin(admin.ModelAdmin):
	list_display = ['status','featured','title', 'created_at',]
# Register your models here.
admin.site.register(Catagory,CatAdmin)
admin.site.register(Blog,BlogAdmin)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(ads)
admin.site.register(About)