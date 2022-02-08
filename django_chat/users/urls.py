from django.urls import path

from django_chat.users.views import UserDetailView, UserUpdateView

app_name = "users"
urlpatterns = [
    path("~update/", view=UserUpdateView.as_view(), name="update"),
    path("<str:uuid>/", view=UserDetailView.as_view(), name="detail"),
]
