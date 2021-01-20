from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from intcCloud.core import views

urlpatterns = [
    path('home/', views.Home.as_view(), name='home'),
    path('', views.signin, name='signin'),
    path('logout/', views.signout, name='signout'),
    path('documents/', views.document_list, name='document_list'),
    path('projects/', views.diploma_list, name='diploma_list'),
    path('documents/upload/', views.upload_document, name='upload_document'),
    path('projects/upload/', views.upload_diploma, name='upload_diploma'),
    path('documents/<int:pk>/', views.delete_document, name='delete_document'),
    path('projects/<int:pk>/', views.delete_diploma, name='delete_diploma'),
    path('big-brother/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
