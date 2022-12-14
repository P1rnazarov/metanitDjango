from django.urls import path, include
from myone import views

product_patterns = [
    path("", views.products),
    path("comments", views.comments),
    path("questions", views.questions),
]

urlpatterns = [
    path("", views.index),
    path("user/", views.user),
    path("products/<int:id>/", include(product_patterns)),
]