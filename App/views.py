#importa as tabelas models que criamos
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.http import HttpResponse
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, BasePermission, SAFE_METHODS

class custom(BasePermission):
    def has_permission(self, request, view):
        user = request.user.id
        customUser = CustomUser.objects.get(user=user)
        customUserSeri = CustomUserSerializer(customUser,many=False)
        tipo = customUserSeri.data['type']
        if(tipo == 'FUNCIONARIO') or request.method in SAFE_METHODS:
            print('Funcionaro')
            return True
        else:
            print("Cliente")
            return False
        
class JustFuncionarios(BasePermission):
    def has_permission(self, request, view):
        user = request.user.id
        customUser = CustomUser.objects.get(user=user)
        customUserSeri = CustomUserSerializer(customUser,many=False)
        tipo = customUserSeri.data['type']
        if(tipo == 'FUNCIONARIO'):
            print('Funcionaro')
            return True
        else:
            print("Cliente")
            return False


class CustomUserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['type', 'user__username', 'data_nasc', 'cpf']
    permission_classes = (IsAuthenticated, )

    def destroy(self, request, *args, **kwargs):
        a = request.get_full_path_info()
        a = a.replace('/customUser/','')
        a = a.replace('/','')
        a = int(a)
        if request.user.is_superuser:
            CustomUserFind = CustomUser.objects.get(id=a)
            CustomUserFind.delete()
            return Response(status=200, data="Deletado!")
        else:
            return Response("Sem Permissão para Excluir um Usuario")

class CategoriaServicoViewSet(ModelViewSet):
    queryset = Categoria_Servico.objects.all()
    serializer_class = Categoria_ServicoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['tipo', 'Valor_Servico']
    permission_classes = (custom, )

class ProdutosManutencaoViewSet(ModelViewSet):
    queryset = Produtos_Manutencao.objects.all()
    serializer_class = Produtos_ManutencaoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['product_name', 'qt_Stock', 'producer_name', 'producer_code', 'Buy_price', 'Sell_price']
    permission_classes = (JustFuncionarios, )

class AutoCategoryViewSet(ModelViewSet):
    queryset = Auto_Category.objects.all()
    serializer_class = Auto_CategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['type']
    permission_classes = (JustFuncionarios, )

class AutoRegisterViewSet(ModelViewSet):
    queryset = Auto_register.objects.all()
    serializer_class = Auto_registerSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category__type', 'marca', 'modelo', 'ano']
    permission_classes = (JustFuncionarios, )

class ManutencionViewSet(ModelViewSet):
    queryset = Manutencion.objects.all()
    serializer_class = ManutencionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['dados_auto__category__type', 'Service_Category__tipo', 'Used_Product__product_name', 'Price_total', 'funcionario_id__user__username', 'Cliente_id__user__username']
    permission_classes = (IsAuthenticated, )

    def create(self, request, *args, **kwargs):

        quantUsed_Product = len(request.data['Used_Product'])
        ValorTotalProduto = 0
        for x in range(quantUsed_Product):
            produto = request.data['Used_Product'][x]
            produtoFind = Produtos_Manutencao.objects.get(id=produto)
            produtoSerilized = Produtos_ManutencaoSerializer(produtoFind, many=False) 

            valorProduto = int(produtoFind['Sell_price'])


            qt_StockProduto = int(produtoSerilized.data['qt_Stock'])
            qt_StockProduto -= 1

            quant_Produ_Used = request.data['Used_Product']
            quant_Produ_Used['qt_Stock'] = qt_StockProduto
            produtoSerilized = Produtos_ManutencaoSerializer(data=quant_Produ_Used,many=False).is_valid(raise_exception=True)
            produtoSerilized.save()

            ValorTotalProduto +=  valorProduto

        print(ValorTotalProduto)

        quant_Service = len(request.data['Service_Category'])
        ValorTotalServico = 0
        for y in range(quant_Service):
            servico = request.data['Service_Category'][y]
            servicoFind = Categoria_Servico.objects.get(id=servico)
            servicoSerialized = Categoria_ServicoSerializer(servicoFind,many=False)
            valorServico = int(servicoSerialized.data['Valor_Servico'])
            ValorTotalServico += valorServico
            
        print(ValorTotalServico)

        valorTotal = ValorTotalProduto+ValorTotalServico

        


        Manutencao = request.data


        Manutencao['Price_total'] = valorTotal
        ManutencionSerialized = ManutencionSerializer(data=Manutencao,many=False)
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
    permission_classes = (custom, )

class PaymentStatusViewSet(ModelViewSet):
    queryset = Payment_Status.objects.all()
    serializer_class = Payment_StatusSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status']
    permission_classes = (custom, )
                
    def get_queryset(self,request, *args, **kwargs):        
        CustomUser.objects.filter(user__id=request.user.id)

        return super().get_queryset()

class PaymentViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category__Payment_type', 'descrition', 'manutention_id', 'status__status', 'discount_value', 'Valor_Final']
    permission_classes = (custom, )

    def create(self, request, *args, **kwargs):
        desconto = float(request.data['discount_value'])
        descontoConvert = desconto/100

        valorManutencaoID = request.data['manutention_id']
        ValorManuFind = Manutencion.objects.get(id=valorManutencaoID)
        ValorManuSeria = ManutencionSerializer(ValorManuFind, many=False)
        ValorManutencao = int(ValorManuSeria.data["Price_total"])
        ValorDescontado = ValorManutencao*descontoConvert

        ValorFinal = ValorManutencao - ValorDescontado

        pagamento = request.data
        pagamento["Valor_Final"] = ValorFinal
        paySeria = PaymentSerializer(pagamento, many=False).is_valid(raise_exception=True)
        paySeria.save() 

        return Response(paySeria.data)





        return super().create(request, *args, **kwargs)