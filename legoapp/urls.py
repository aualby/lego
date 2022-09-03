from django.urls import path
from . import views
# from .views import index

urlpatterns = [
        # Rendered static pages
        path('', views.index, name='index'),
]
