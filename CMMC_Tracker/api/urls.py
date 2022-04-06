from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('org-overview/', views.organization_view, name="org-overview"),
    path('controls-overview/', views.controls_overview, name="controls-overview"),
    path('control-view/<str:pk>/', views.control_view, name="control-view"),
    path('update-control/<str:pk>/', views.update_control, name="update-control"),
]