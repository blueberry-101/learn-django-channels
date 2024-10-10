from django.shortcuts import render

# Create your views here.
def chatroom(request,groupname):
    context = {"group_name":groupname}
    return render(request=request,template_name="app/index.html",context=context)