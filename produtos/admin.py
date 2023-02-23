from django.contrib import admin
from produtos.models import Produto, Anunciante

# Register your models here.
admin.site.register(Produto)
admin.site.register(Anunciante)