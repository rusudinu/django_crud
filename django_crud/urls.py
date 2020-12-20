from django.contrib import admin
from django.urls import path
from .crud_app import views

urlpatterns = [
    path('', views.main_page),  # the main page, where all the projects are listed
    path('new/', views.new_project),  # add a new project
    path('project/', views.display_project),  # display the page of a project
    path('update/', views.update),  # update a project
    path('delete/', views.delete),  # delete a project
    path('create/', views.create),  # create a project
    path('read/', views.read),  # read a project
    path('work/', views.work),  # showcase of the projects | similar with read
    path('mobile/', views.mobile),  # showcase of the mobile projects | similar with read
    path('web/', views.web),  # showcase of the web projects | similar with read
    path('awards/', views.awards),  # showcase of the awards
    path('about/', views.about),  # about page
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
