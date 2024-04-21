from django.shortcuts import render
from myapp.models import Group, Chats
# Create your views here.
def chatroom(request,groupname):
    group_qset = Group.objects.filter(name = groupname).first()
    # this line retrieves the first Group object with a specific name from the database, if it exists, or None if no such group is found.
    # group_qset = Group.objects.filter(name = groupname) this cannot be written because it returns queryset if found.
    chats = ()
    if group_qset:
        print(f"This group {groupname} already exists")
        chats = Chats.objects.filter(group = group_qset)
    else:
        group_model = Group(name=groupname)
        group_model.save()

    context = {"group_name":groupname,"chats":chats}
    return render(request=request,template_name="app/index.html",context=context)