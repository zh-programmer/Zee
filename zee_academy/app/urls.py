from django.urls import path
from .import views
from .views import Home_View , Free_View , P_Courses , P_Courses_View


urlpatterns = [
	# path("" , views.home , name = "home")
	# path("courses/" , views.Paid_View , name = "paid_courses")
	path("" , Home_View.as_view() , name = "home"),
	path("free-tutorial/<int:pk>" , Free_View.as_view() , name = "free_view"),
	path("Courses/" , P_Courses.as_view() , name = "paid_courses"),
	path("Courses/<int:pk>" , P_Courses_View.as_view() , name = "paid_courses_view"),
	path("About_Us" , views.About_US_View , name = "about_us"),
]
