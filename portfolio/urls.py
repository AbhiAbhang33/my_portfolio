from django.urls import path
from django_distill import distill_path
from .views import home

# This function tells django-distill the parameters required for the `home` view
def get_index():
    return None  # `None` because no parameters are required

urlpatterns = [
    distill_path('', home, name='home', distill_func=get_index),
]