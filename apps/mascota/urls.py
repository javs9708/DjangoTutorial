
from django.conf.urls import  url, include
from apps.mascota.views import *
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^$',index,name='index'),
    url(r'^nuevo$', login_required(MascotaCreate.as_view()), name='mascota_crear'),
    url(r'^vacuna$',login_required(vacuna_view), name='vacuna_crear'),
    url(r'^listar$',login_required(MascotaList.as_view()), name='mascota_listar'),
    url(r'^editar/(?P<id_mascota>\d+)/$',login_required(mascota_edit), name='mascota_editar'),
    url(r'^eliminar/(?P<id_mascota>\d+)/$',login_required(mascota_delete), name='mascota_eliminar'),

]
