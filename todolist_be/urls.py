from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('authorization/', include('user.urls')),
    path('admin/', admin.site.urls),
    path('user/', include('user.urls'))
]
