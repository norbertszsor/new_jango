from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path(r'^admin/', admin.site.urls),
    path('',include('cinemaHall_app.urls')),
    url(r'^api-auth/', include('rest_framework.urls'))
]
