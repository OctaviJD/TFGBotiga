from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$', views.recipe_list, name='recipe_list'),
]