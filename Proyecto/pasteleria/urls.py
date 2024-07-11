from django.contrib import admin
from django.urls import path
from core.views import homeView
from contacto.views import contactViews
from crearusuario.views import createUsersViews
from login.views import login_view
from read.views import mostrar_inventario
from update.views import updateViews
from carro.views import carroViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homeView, name='home'),
    path('contacto', contactViews, name='contacto'),
    path('create', createUsersViews, name='createUsers'),
    path('login/', login_view, name="login"),
    path('inventario/', mostrar_inventario, name='mostrar_inventario'),
    path('update/', updateViews, name='actualizar'),
    path('carro', carroViews, name="carro")
]
