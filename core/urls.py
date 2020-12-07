from django.urls import path
from .views import home
from .views import formulario
from .views import nosotros
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name="home"),
    path('formulario/' , formulario, name="formulario"),
    path('nosotros/', nosotros, name="nosotros"),
    ]+static(settings.STATIC_URL, document_root = settings.STATIC_ROOT) 

  