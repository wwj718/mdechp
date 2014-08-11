from django.contrib import admin

# Register your models here.
from django.contrib import admin
from models import MpttMeetInfo , Owner ,Meet


class MpttMeetInfoAdmin(admin.ModelAdmin):
    tree_auto_open = 0
    list_display = ('title',)
    ordering = ('title',)

class OwnerAdmin(admin.ModelAdmin):
    fields = ('name','meetInfo' )
    list_display = ('name','meetInfo')

class MeetAdmin(admin.ModelAdmin):
    fields = ('name','meetInfo' )
    list_display = ('name','meetInfo')



admin.site.register(Owner, OwnerAdmin)

admin.site.register(Meet, MeetAdmin)

admin.site.register(MpttMeetInfo,MpttMeetInfoAdmin)