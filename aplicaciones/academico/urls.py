from django.urls import path

from . import views
# para cargar Images



urlpatterns = [
    path('', views.home, name='home'),
    path('registrarCurso', views.registrarCurso),
    path('editarCurso/<codigo>', views.editarCurso),
    path('editCurso/', views.editCurso),
    path('eliminarCurso/<codigo>', views.eliminarCurso),
]

# Configure the custom 404 view
handler404 = views.custom_404