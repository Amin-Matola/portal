from django.urls import path, include
from apps.restraunts import views

urlpatterns = [
    path("", views.restraunts, name="restraunts"),
    path("add", views.add, name="add"),
    path("delete/<int:restraunt>", views.delete, name="delete")
]