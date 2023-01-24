from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Student


def Home(req):
	return render(req,"Home.html")


def About(req):
	return render(req,"About.html")

def Contact(req):
	return render(req,"Contact.html")

def insertTask(req):
	name=req.GET.get("name")
	email=req.GET.get("email")
	mobile=int(req.GET.get("mobile"))
	ob=Student()
	ob.name=name
	ob.email=email
	ob.mobile=mobile
	ob.save()
	return redirect("/blog/Contact")