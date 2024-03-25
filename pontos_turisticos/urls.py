from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from pontos_turisticos.api.viewSets import PontoTuristicoViewSet

router = routers.DefaultRouter() # Cria um objeto de roteamento padrão
router.register(r'pontos_turisticos', PontoTuristicoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
