from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
	def get(self, request, **kwargs):
		a = 2+3
		print (a)
		print("information")
		num_books = "Hello I am Python %s" %a
		return render(request, 'home.html', 
			context={'num_books':num_books},
			)
