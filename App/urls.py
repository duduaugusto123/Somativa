#importando a biblioteca de 'caminhos' do django
from django.urls import path
#importando as views que criamos da nossa api:
from .views import *
from rest_framework.routers import DefaultRouter
from .views import ProdutosComBaixoEstoqueListView

router = DefaultRouter()
router.register(r'manutencion', ManutencionViewSet)
router.register(r'customUser', CustomUserViewSet)
router.register(r'categoria_Servico', CategoriaServicoViewSet)
router.register(r'produtos_Manutencao', ProdutosManutencaoViewSet)
router.register(r'dados_auto', AutoRegisterViewSet)
router.register(r'auto_Category', AutoCategoryViewSet)
router.register(r'payment_Category', PaymentCategoryViewSet)
router.register(r'payment_Status', PaymentStatusViewSet)
router.register(r'payment', PaymentViewSet)



urlpatterns = [    
    path('produtos-com-baixo-estoque/', ProdutosComBaixoEstoqueListView.as_view(), name='produtos-com-baixo-estoque'),
]

urlpatterns += router.urls

