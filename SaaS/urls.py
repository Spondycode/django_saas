from django.contrib import admin
from django.urls import path, include
from user.views import *

urlpatterns = [
    path("", home, name="home"),
    path("admin/", admin.site.urls),
    path("user/", include("user.urls")),
    path("course/", include("course.urls")),
    path("payment/", include("payment.urls")),
]
