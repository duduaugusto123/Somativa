#importa as tabelas models que criamos
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.http import HttpResponse
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, BasePermission

class CustomUserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['type', 'user__username', 'data_nasc', 'cpf']
    permission_classes = (IsAuthenticated, )

class CategoriaServicoViewSet(ModelViewSet):
    queryset = Categoria_Servico.objects.all()
    serializer_class = Categoria_ServicoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['tipo', 'Valor_Servico']
    permission_classes = (IsAuthenticated, )

class ProdutosManutencaoViewSet(ModelViewSet):
    queryset = Produtos_Manutencao.objects.all()
    serializer_class = Produtos_ManutencaoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['product_name', 'qt_Stock', 'producer_name', 'producer_code', 'Buy_price', 'Sell_price']
    permission_classes = (IsAuthenticated, )

class AutoCategoryViewSet(ModelViewSet):
    queryset = Auto_Category.objects.all()
    serializer_class = Auto_CategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['type']
    permission_classes = (IsAuthenticated, )

class AutoRegisterViewSet(ModelViewSet):
    queryset = Auto_register.objects.all()
    serializer_class = Auto_registerSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category__type', 'marca', 'modelo', 'ano']
    permission_classes = (IsAuthenticated, )

class ManutencionViewSet(ModelViewSet):
    queryset = Manutencion.objects.all()
    serializer_class = ManutencionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['dados_auto__category__type', 'Service_Category__tipo', 'Used_Product__product_name', 'Price_total', 'funcionario_id__user__username', 'Cliente_id__user__username']
    permission_classes = (IsAuthenticated, )
    def create(self, request, *args, **kwargs):
        produto = request.data['Used_Product']
        servico = request.data['Service_Category']
        produtoFind = Produtos_Manutencao.objects.get(id=produto)
        servicoFind = Categoria_Servico.objects.get(id=servico)
        produtoSerilized = Produtos_ManutencaoSerializer(produtoFind, many=False)
        valorProduto = float(produtoSerilized.data['Sell_price'])
        servicoSerialized = Categoria_ServicoSerializer(servicoFind,many=False)
        valorServico = float(servicoSerialized.data['Valor_Servico'])
        valorTotal = valorProduto+valorServico
        request.data['Price_total'] = valorTotal
        ManutencionSerialized = ManutencionSerializer(data=request.data,many=False)
        ManutencionSerialized.is_valid(raise_exception=True)
        ManutencionSerialized.save()

        funcionario = request.data['funcionario_id']
        teste = CustomUser.objects.get(user=funcionario)
        a = CustomUserSerializer(teste,many=False)
        
        if a.data['type'] == 'FUNCIONARIO':
            print("é funcionario")
            ManutencionSerialized.save()
        else:
            return Response('Não é funcionario!')
        return Response(ManutencionSerialized.data)

class PaymentCategoryViewSet(ModelViewSet):
    queryset = Payment_Category.objects.all()
    serializer_class = Payment_CategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['Payment_type']
    permission_classes = (IsAuthenticated, )

class PaymentStatusViewSet(ModelViewSet):
    queryset = Payment_Status.objects.all()
    serializer_class = Payment_StatusSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status']
    permission_classes = (IsAuthenticated, )

class PaymentViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category__Payment_type', 'descrition', 'manutention_id', 'status__status', 'discount_value', 'Valor_Final']
    permission_classes = (IsAuthenticated, )