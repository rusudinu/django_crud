from django.contrib import admin
from django.urls import path
from .crud_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test_404/', views.error_404),
    path('test_403/', views.error_403),
    path('test_400/', views.error_400),
    path('test_500/', views.error_500),
]

handler404 = views.error_404
handler500 = views.error_500
handler403 = views.error_403
handler400 = views.error_400
