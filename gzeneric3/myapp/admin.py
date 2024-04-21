from django.contrib import admin
from myapp.models import Chats, Group
# Register your models here.
@admin.register(Chats)
class ChatAdmin(admin.ModelAdmin):
    list_display = ["group","texts","timestamp"]

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ["name"]