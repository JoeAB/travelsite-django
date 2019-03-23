from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('/details/<str:countryID>', views.details),
	path('/viewPost/<int:postID>', views.viewPost),
]
