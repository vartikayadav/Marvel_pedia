from django.contrib import admin
from .models import Comics
# Register your models here.
class ComicsAdmin(admin.ModelAdmin):
    list_display=['title','slug','price','stock','available','created','updated']
    list_editable=['price','stock','available']
    prepopulated_fields={'slug':('title',)}
    list_per_page=100
admin.site.register(Comics,ComicsAdmin)
