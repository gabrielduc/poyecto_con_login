#from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views





urlpatterns = [

   
  
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('index', views.index, name='index'),
    path('Servicios', views.Servicios, name='Servicios'),
    path('Nosotros', views.Nosotros, name='Nosotros'),
    path('Entrenadores', views.Entrenadores, name='Entrenadores'),
    path('Contactanos', views.Contactanos, name='Contactanos'),
    path('tabla_entrenadores/', views.TablaEntrenadores, name='tabla_entrenadores'),
    path('eliminar_alumno/<int:alumno_id>/', views.eliminar_alumno, name='eliminar_alumno'),
    path('agregar_cliente_gimnasio/<int:profesional_id>/', views.agregar_cliente_gimnasio, name='agregar_cliente_gimnasio'),

]
    
                         