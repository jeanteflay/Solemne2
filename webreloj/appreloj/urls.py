from django.urls import path
from . import views
urlpatterns = [
    path('',views.avance1 , name = "avance"),
    path('contacto/',views.Contacto , name = "contacto"),
    path('quienessomos/',views.QuienesSomos , name = "quienesomos"),
    path('registro/',views.Register , name = "registro")
]