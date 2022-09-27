from django.contrib import admin
from django.urls import path , include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('info/', views.info),
    path('', include('Handover.urls')),

]

urlpatterns += staticfiles_urlpatterns()
