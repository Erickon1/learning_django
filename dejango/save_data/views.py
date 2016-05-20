from django.shortcuts import render, get_objet_or_404, redirect
from .models import *



# Create your views here.
class GetUser(View):
	def get(self,request):
		template = "templates/main.html"
		return render(request,template)

	
	def post(self,request):
		name= request.POST.get('name','')
		email= request.POST.get('email','')
		user_data = User(
			name=name,
			email=email,
			)
		user_data.save()
		return redirect('http://127.0.0.1:8000')


