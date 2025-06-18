
from django.contrib import admin
from django.urls import include, path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("myapp.urls"))
]
