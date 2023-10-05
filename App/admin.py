from django.contrib import admin
from .models import * 

# Register your models here.


class detCustomUser(admin.ModelAdmin):
    list_display = ('id', 'type', 'user', 'cpf')
    list_display_links = list_display
    search_fields = ('type', 'user',)
    list_per_page = 10
#registra as configurações realizadas do model na página de admin
admin.site.register(CustomUser,detCustomUser)

class detCategoria_Servico(admin.ModelAdmin):
    list_display = ('id', 'tipo', 'Valor_Servico')
    list_display_links = list_display
    search_fields = ('tipo', 'Valor_Servico',)
    list_per_page = 10
#registra as configurações realizadas do model na página de admin
admin.site.register(Categoria_Servico,detCategoria_Servico)

class detProdutos_Manutencao(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'qt_Stock','producer_name','producer_code','Buy_price')
    list_display_links = list_display
    search_fields = ('product_name', 'qt_Stock','producer_name',)
    list_per_page = 10
#registra as configurações realizadas do model na página de admin
admin.site.register(Produtos_Manutencao,detProdutos_Manutencao)

class detAuto_Category(admin.ModelAdmin):
    list_display = ('id', 'type')
    list_display_links = list_display
    search_fields = ('type',)
    list_per_page = 10
#registra as configurações realizadas do model na página de admin
admin.site.register(Auto_Category,detAuto_Category)

class detAuto_register(admin.ModelAdmin):
    list_display = ('id', 'category','marca','modelo','ano')
    list_display_links = list_display
    search_fields = ('category','marca','modelo',)
    list_per_page = 10
#registra as configurações realizadas do model na página de admin
admin.site.register(Auto_register,detAuto_register)

class detManutencion(admin.ModelAdmin):
    list_display = ('id', 'dados_auto','Price_total','funcionario_id','Cliente_id')
    list_display_links = ('id', 'dados_auto','Price_total','funcionario_id','Cliente_id')
    search_fields = ('dados_auto','Price_total','funcionario_id','Cliente_id','Used_Product',)
    list_per_page = 10
#registra as configurações realizadas do model na página de admin
admin.site.register(Manutencion,detManutencion)

class detPayment_Category(admin.ModelAdmin):
    list_display = ('id', 'Payment_type')
    list_display_links = list_display
    search_fields = ('Payment_type',)
    list_per_page = 10
#registra as configurações realizadas do model na página de admin
admin.site.register(Payment_Category,detPayment_Category)

class detPayment_Status(admin.ModelAdmin):
    list_display = ('id', 'status')
    list_display_links = list_display
    search_fields = ('status',)
    list_per_page = 10
#registra as configurações realizadas do model na página de admin
admin.site.register(Payment_Status,detPayment_Status)

class detPayment(admin.ModelAdmin):
    list_display = ('id', 'category','descrition','manutention_id','status','discount_value','Valor_Final')
    list_display_links = list_display
    search_fields = ('category','descrition','manutention_id','status','Used_Product',)
    list_per_page = 10
#registra as configurações realizadas do model na página de admin
admin.site.register(Payment,detPayment)