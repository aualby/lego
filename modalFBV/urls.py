from django.urls import path
from . import views

urlpatterns = [
        # Rendered static pages
        path('', views.modalfbv_index, name='modalfbv-index'),
        path('projects/', views.project_list, name='project_list'),
        path('projects/add', views.add_project, name='add_project'),
        path('projects/<int:pk>/remove', views.remove_project, name='remove_project'),
        path('projects/<int:pk>/edit', views.edit_project, name='edit_project'),
]
