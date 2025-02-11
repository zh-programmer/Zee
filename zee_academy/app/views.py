from django.shortcuts import render 
from django.views.generic import ListView , DetailView 
from .models import Free_Tutorials , Paid_Courses


# Home Page
class Home_View(ListView):
	model = Free_Tutorials
	template_name = "index.html"
	ordering = ['-id']

# Free Tutorial Page
class Free_View(DetailView):
	model = Free_Tutorials
	template_name = "free_view.html"


class P_Courses(ListView):
	model = Paid_Courses
	template_name = "paid_courses.html"


class P_Courses_View(DetailView):
	model = Paid_Courses
	template_name = "paid_courses_view.html"

def About_US_View(request):
	return render(request , "about_us.html" , {})