from django.contrib import admin
from django.urls import path
from django.conf.urls import include
import chatapp

urlpatterns = [
    path('chat/', include('chatapp.urls')),
    path('accounts/', include("django.contrib.auth.urls")),
    path('admin/', admin.site.urls),
    path('register/', chatapp.views.register, name='register'),
]
