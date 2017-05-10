from django.conf.urls import url
from . import views
from django.views.generic import ListView, DetailView
from display.models import Entry

urlpatterns = [
    #url(r'^$',views.index, name='index')
    url(r'^$', ListView.as_view(
        queryset=Entry.objects.all().order_by("id"),
    	template_name="entry.html")), 
]