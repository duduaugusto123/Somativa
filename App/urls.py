#importando a biblioteca de 'caminhos' do django
from django.urls import path
#importando as views que criamos da nossa api:
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'manutencion', ManutencionViewSet)
router.register(r'customUser', CustomUserViewSet)
router.register(r'categoria_Servico', CategoriaServicoViewSet)
router.register(r'produtos_Manutencao', ProdutosManutencaoViewSet)
router.register(r'dados_auto', AutoRegisterViewSet)
router.register(r'auto_Category', AutoCategoryViewSet)



urlpatterns = router.urls