from django.urls import path
from main import views

urlpatterns = [
    path('',views.greetings),
    path('download/',views.download),
]
