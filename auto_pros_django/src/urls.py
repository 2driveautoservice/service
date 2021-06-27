from django.urls import path

from . import views

#Luke: Allows you to create urls for objects or slugs

urlpatterns = [
    path('get-company-boxes/', views.CompanyBoxList.as_view()),
    path('get-locations/', views.LocationList.as_view()),
    path('get-service-categories/', views.CategoryServiceList.as_view())
]