from portfolio import views
from django_distill import distill_path

urlpatterns = [
    distill_path('', views.get_index, name='home'),
]
