from.import views
from django.urls import path

urlpatterns = [
    path("",views.employment_feedback,name="homepage"),
    path("homepage",views.employment_feedback,name="homepage"),
    path("program_details",views.program_details,name="program_details"),
    path("cityevent",views.cityevent,name="cityevent"),
    path("feedback",views.feedback,name="feedback"),
    path("about",views.about,name="about"),
    path("contact",views.contact,name="contact")
]
