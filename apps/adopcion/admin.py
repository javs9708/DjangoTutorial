from django.contrib import admin


from apps.adopcion.models import Persona, Solicitud


@admin.register(Persona)
class adminMascota(admin.ModelAdmin):
    list_display=['nombre' , 'apellidos', 'edad', 'telefono', 'email', 'domicilio']

@admin.register(Solicitud)
class adminMascota(admin.ModelAdmin):
    list_display=['persona' , 'numero_mascotas', 'razones']
