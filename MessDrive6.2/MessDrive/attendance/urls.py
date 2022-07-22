from django.urls import path
from .import views
#from django.core.urlresolvers import reverse_lazy

urlpatterns = [
    path('expense', views.expense, name = "expense"),
    path('present', views.markPresent, name = "markPresent"),

]