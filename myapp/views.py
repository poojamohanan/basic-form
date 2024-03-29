from django.shortcuts import render,redirect
from . models import Member

def index(request):
    members=Member.objects.all()
    context={"members": members}
    return render(request,'index.html',context)

def create(request):
    member=Member(firstname=request.POST['firstname'],lastname=request.POST['lastname'])
    member.save()
    return redirect('/')

def edit(request,id):
    members=Member.objects.get(id=id)
    context={"members" : members}
    return render(request,'edit.html',context)

def update(request,id):
    member=Member.objects.get(id=id)
    member.firstname=request.POST['firstname']
    member.lastname = request.POST['lastname']
    member.save()
    return redirect('/myapp/')

def delete(request,id):
    member=Member.objects.get(id=id)
    member.delete()
    return redirect('/myapp/')
